import os, json

ASSETS_DIR = "Assets/Common/UI/Custom/"
CLIENT_ASSETS_DIR = "Interface/"

# Every element contains File (path to parsed file, relative to ASSETS_DIR) and LineNumber (1-indexed) and IsClient (this is a boolean, if true the only usages found were in the client)
# For Types and UIElements, these are where it was first used, since they are not declared in .ui files

# ImportedFiles
# - Alias: What the file was imported as
# - ImportedFile: Path to imported file (relative to ASSETS_DIR)

# Variables
# - Name: Variable name
# - Value: Value, may be multiple lines (will be a single string potentially containing new line characters)

# Types (some might be functions, idk, this is for things like LabelStyle)
# - Name: Type name
# ExampleFields:
#   FieldName:
#      ExampleValues: List of all found values

# UIElements (this is for things like Button, Label)
# - Name: Element name
# ExampleFields:
#   FieldName:
#      ExampleValues: List of all found values

data = {
    "ImportedFiles": [],
    "Variables": [],
    "Types": [],
    "UIElements": []
}

foundTypeNames = {}
foundUIElements = {}

# checks for ; which isn't commented
def is_line_terminated(s):
    i = s.find(";")
    if i == -1:
        return False
    return "//" not in s[:i]


def resolve_import(path, importedPath):
    return os.path.normpath(os.path.join(os.path.dirname(path), importedPath))


# get variable value
def extract_value(lines, start_index, first_line_offset):
    result = []
    i = start_index
    line = lines[i][first_line_offset:]
    result.append(line)
    open_braces = line.count("{") - line.count("}")
    open_parens = line.count("(") - line.count(")")
    if open_braces == 0 and open_parens == 0 and ";" in line:
        return line.rstrip(";\n").strip()
    i += 1
    while i < len(lines):
        line = lines[i]
        result.append(line)
        open_braces += line.count("{") - line.count("}")
        open_parens += line.count("(") - line.count(")")
        if open_braces <= 0 and open_parens <= 0 and ";" in line:
            break
        i += 1
    joined = "".join(result)
    if joined.rstrip().endswith(";"):
        joined = joined.rstrip()[:-1]
    return joined.strip()

def add_common(d: dict, path: str, line_index: int, is_client: bool):
    d["File"] = path
    d["LineNumber"] = line_index + 1
    d["IsClient"] = is_client

def get_type_fields(lines: list, line_index: int, typeEndIndex: int):
    line = lines[line_index][typeEndIndex:] # cut off everything before the type on the first line
    params = ""

    # extract params into a big string
    for i in range(line_index, len(lines)):
        if i != line_index:
            line = lines[i]

        params += line

        if is_line_terminated(line):
            break

    params = params[:params.rfind(");")] # remove line terminator

    # convert string to dict
    currentKey = ""
    currentVal = ""
    isKey = True
    nest = 0
    fields = {}
    for c in params:
        if c == "(":
            nest += 1
        if c == ")":
            nest -= 1
        if nest == 0:
            if isKey and c == ":":
                isKey = False
                continue
            if not isKey and c == ",":
                fields[currentKey] = currentVal
                currentKey = ""
                currentVal = ""
                isKey = True
                continue
        if isKey:
            currentKey += c
        else:
            currentVal += c

    if currentKey != "":
        fields[currentKey] = currentVal
    
    # clean up keys and values
    cleanedFields = {}
    for k, v in fields.items():
        k = k.replace("\n", "").strip()
        v = v.strip()

        cleanedFields[k] = v

    return cleanedFields

def parse_types(path: str, lines: list, line_index: int, is_client: bool):
    types = lines[line_index].split("(")
    indexInLine = 0
    for i in range(len(types) - 1): # last type doesn't have a ( after so probably not a type
        indexInLine += len(types[i])
        typeName = types[i].split(" ").pop() # get the thing after the last space
        if len(typeName) == 0 or typeName.isspace(): # Type is empty space
            continue
        if "#" in typeName:
            continue # Hex color code
        
        t = {}
        if typeName not in foundTypeNames:
            foundTypeNames[typeName] = t
            add_common(t, path, line_index, is_client)
            t["Name"] = typeName
            t["Fields"] = {}
            data["Types"].append(t)
        else:
            t = foundTypeNames[typeName]

        for k, v in get_type_fields(lines, line_index,  indexInLine + 1).items():
            if len(k) == 0 or k.isspace():
                continue
            if k not in t["Fields"]:
                t["Fields"][k] = {"ExampleValues": set()}

            t["Fields"][k]["ExampleValues"].add(v)

def convert_field_sets_to_lists():
    for foundType in data["Types"]:
        for field in foundType["Fields"].values():
            field["ExampleValues"] = list(field["ExampleValues"])

    for uiElement in data["UIElements"]:
        for field in uiElement["Fields"].values():
            field["ExampleValues"] = list(field["ExampleValues"])

def has_equals_before_semicolon(line: str, startIndex: int) -> bool:
    for i in range(startIndex, len(line)):
        if line[i] == "=":
            return True
        if line[i] == ";":
            return False
    return False

def get_all_fields_of_element(lines: list, line_index: int, bracketIndex: int):
    # cut off everything before the bracket on the first line
    line = lines[line_index][bracketIndex + 1:]
    nest = 1
    params = ""
    foundBrackets = [] # [open bracket index, close bracket index]
    bracketStack = [] # indices into foundBrackets
    isUIID = False # if the current character is part of an id (including the #)

    # extract params into a big string
    for i in range(line_index, len(lines)):
        if i != line_index:
            line = lines[i]

        for c in line:
            if isUIID and c.isspace():
                isUIID = False
            if c == "#":
                if params[len(params) - 2] == ":":
                    params += c # False alarm, hex colour code, not an id!
                    continue
                isUIID = True
            if isUIID:
                continue
            if c == "{":
                nest += 1
                bracketStack.append(len(foundBrackets))
                foundBrackets.append([len(params), -1])
            elif c == "}":
                nest -= 1
                if len(bracketStack) > 0: # not the final bracket
                    foundBrackets[bracketStack.pop()][1] = len(params)
            params += c
            if nest <= 0:
                break
        if nest <= 0:
            break

    params = params[:params.rfind("}") - 1] # remove final bracket
    # remove all found nested ui elements
    params = list(params)
    for start, end in foundBrackets:
        # move start backwards from the { until the start of the ui element
        i = start - 1

        while i >= 0 and params[i].isspace():
            i -= 1  # ignore whitespace before bracket

        # ok now we found either the ID or ui element name
        if i >= 0 and params[i] == "#":
            # it was an id, keep going
            i -= 1
            while i >= 0 and params[i].isspace():
                i -= 1  # ignore whitespace before id

        while i >= 0 and not params[i].isspace():
            i -= 1

        for j in range(i + 1, end + 1):
            params[j] = " "


    # parse local variables
    # TODO this is limited because most variables are declared above not inside the ui element
    variables = {}
    isVar = False
    isVarName = False
    varName = ""
    varValue = ""
    for i in range(len(params)):
        if params[i].isspace():
            continue
        if params[i] == "@" and not isVar and not isVarName and has_equals_before_semicolon(params, i + 1):
            isVar = True
            isVarName = True
            params[i] = ""
            continue
        if not isVar:
            continue
        if isVarName and params[i] == "=":
            isVarName = False
            params[i] = ""
            continue
        if not isVarName and params[i] == ";":
            isVar = False
            variables[varName] = varValue
            varName = ""
            varValue = ""
            params[i] = ""
            continue
        if isVarName:
            varName += params[i]
        else:
            varValue += params[i]
        params[i] = ""

    params = "".join(params)

    # replace variables
    for k, v in variables.items():
        continue
        params = params.replace("@" + k, v)

    # build a dictionary
    fields = {}
    currentKey = ""
    currentVal = ""
    isKey = True
    for c in params:
        if c.isspace():
            continue
        if c == ":" and isKey:
            isKey = False
            continue
        if c == ";" and not isKey:
            isKey = True
            fields[currentKey] = currentVal
            currentKey = ""
            currentVal = ""
            continue
        if isKey:
            currentKey += c
        else:
            currentVal += c

    return fields

def parse_ui_elements(path: str, lines: list, line_index: int, is_client: bool):
    line = lines[line_index]
    indexOfBracket = line.rfind("{")
    if indexOfBracket < 1:
        return  # either no bracket or it is the first character
    
    line = line.rstrip()
    if not line.endswith("{"):
        return # non whitespace character after {
    
    if line[indexOfBracket - 1] == " ":
        line = line[:-2]
    else:
        line = line[:-1]

        
    lastSpaceIndex = line.rfind(" ")
    if lastSpaceIndex == -1:
        return
    
    lastHashtagIndex = line.rfind("#")
    if lastHashtagIndex > lastSpaceIndex:
        # we have an id, need to remove it
        line = line[:-(len(line) - lastHashtagIndex)] # remove the id
        line = line.rstrip()
        lastSpaceIndex = line.rfind(" ") # this is okay to be -1, it means ui element name is the whole line
    
    uiElementName = line[lastSpaceIndex + 1:]
    if len(uiElementName) == 0 or uiElementName.isspace():
        return
    
    elem = {}
    if uiElementName not in foundUIElements:
        add_common(elem, path, line_index, is_client)
        elem["Name"] = uiElementName
        elem["Fields"] = {}
        data["UIElements"].append(elem)
        foundUIElements[uiElementName] = elem
    else:
        elem = foundUIElements[uiElementName]

    for key, value in get_all_fields_of_element(lines, line_index, indexOfBracket).items():
        if key not in elem["Fields"]:
            elem["Fields"][key] = {"ExampleValues": set()}
        elem["Fields"][key]["ExampleValues"].add(value)

def parse_imports(path: str, lines: list, tokens: list, line_index: int, is_client: bool):
    line = lines[line_index]
    if len(tokens) < 3:
        return False
    if not line.startswith("$"):
        return False
    i = {}
    add_common(i, path, line_index, is_client)
    i["Alias"] = tokens[0][1:]
    importedPath = tokens[2][:tokens[2].find(";")]
    i["ImportedFile"] = resolve_import(path, importedPath)
    data["ImportedFiles"].append(i)
    return True
    

def parse_var(path: str, lines: list, tokens: list, line_index: int, is_client: bool):
    if len(tokens) < 3 or not tokens[0].startswith("@") or tokens[1] != "=":
        return
    var = {}
    var["Name"] = tokens[0][1:]
    var["Value"] = extract_value(lines, line_index, lines[line_index].find(tokens[2]))
    add_common(var, path, line_index, is_client)
    data["Variables"].append(var)

def parse_file(path: str, asset_dir: str, is_client: bool):
    with open(asset_dir + path, "r") as file:
        if is_client:
            path = "Client/Data/Game/" + asset_dir + path
        lines = file.readlines()
        for line_index in range(len(lines)):
            tokens = lines[line_index].split(" ")

            if parse_imports(path, lines, tokens, line_index, is_client):
                continue

            parse_types(path, lines, line_index, is_client)

            parse_ui_elements(path, lines, line_index, is_client)

            parse_var(path, lines, tokens, line_index, is_client)

def parse_all_ui_files():
    for root, _, files in os.walk(ASSETS_DIR):
        for file in files:
            if not file.endswith(".ui"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ASSETS_DIR)
            if rel_path == "Test.ui":
                continue
            parse_file(rel_path, ASSETS_DIR, False)

    # parse server first so anything on the server is marked as IsClient=False
    for root, _, files in os.walk(CLIENT_ASSETS_DIR):
        for file in files:
            if not file.endswith(".ui"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, CLIENT_ASSETS_DIR)
            if rel_path == "Test.ui":
                continue
            parse_file(rel_path, CLIENT_ASSETS_DIR, True)

#parse_file("Test.ui")

parse_all_ui_files()

convert_field_sets_to_lists()
with open("out.json", "w") as file:
    file.write(json.dumps(data, indent=4))

import gen_docs