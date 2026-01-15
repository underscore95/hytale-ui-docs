import os, json

ASSETS_DIR = "Assets/Common/UI/Custom/"

# Every element contains File (path to parsed file, relative to ASSETS_DIR) and LineNumber (1-indexed)
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

data = {
    "ImportedFiles": [],
    "Variables": [],
    "Types": [],
    "UIElements": []
}

foundTypeNames = {}
foundUIElements = set()

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

def add_common(d: dict, path: str, line_index: int):
    d["File"] = path
    d["LineNumber"] = line_index + 1

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

def parse_types(path: str, lines: list, line_index: int):
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
            add_common(t, path, line_index)
            t["Name"] = typeName
            t["Fields"] = {}
            data["Types"].append(t)
        else:
            t = foundTypeNames[typeName]

        for k, v in get_type_fields(lines, line_index,  indexInLine + 1).items():
            if k not in t["Fields"]:
                t["Fields"][k] = {"ExampleValues": set()}

            t["Fields"][k]["ExampleValues"].add(v)

def convert_field_sets_to_lists():
    for foundType in data["Types"]:
        for field in foundType["Fields"].values():
            field["ExampleValues"] = list(field["ExampleValues"])

def parse_ui_elements(path: str, lines: list, line_index: int):
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
        line.rstrip()
        lastSpaceIndex = line.rfind(" ")
        if lastSpaceIndex == -1:
            return
    
    uiElementName = line[lastSpaceIndex + 1:]
    if len(uiElementName) == 0 or uiElementName.isspace():
        return
    
    if uiElementName in foundUIElements:
        return
    foundUIElements.add(uiElementName)

    elem = {}
    add_common(elem, path, line_index)
    elem["Name"] = uiElementName
    data["UIElements"].append(elem)

def parse_imports(path: str, lines: list, tokens: list, line_index: int):
    line = lines[line_index]
    if len(tokens) < 3:
        return False
    if not line.startswith("$"):
        return False
    i = {}
    add_common(i, path, line_index)
    i["Alias"] = tokens[0][1:]
    importedPath = tokens[2][:tokens[2].find(";")]
    i["ImportedFile"] = resolve_import(path, importedPath)
    data["ImportedFiles"].append(i)
    return True
    

def parse_var(path: str, lines: list, tokens: list, line_index: int):
    if len(tokens) < 3 or not tokens[0].startswith("@") or tokens[1] != "=":
        return
    var = {}
    var["Name"] = tokens[0][1:]
    var["Value"] = extract_value(lines, line_index, lines[line_index].find(tokens[2]))
    add_common(var, path, line_index)
    data["Variables"].append(var)

def parse_file(path: str):
    with open(ASSETS_DIR + path, "r") as file:
        lines = file.readlines()
        for line_index in range(len(lines)):
            tokens = lines[line_index].split(" ")

            if parse_imports(path, lines, tokens, line_index):
                continue

            parse_types(path, lines, line_index)

            parse_ui_elements(path, lines, line_index)

            parse_var(path, lines, tokens, line_index)

def parse_all_ui_files():
    for root, _, files in os.walk(ASSETS_DIR):
        for file in files:
            if not file.endswith(".ui"):
                continue
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, ASSETS_DIR)
            parse_file(rel_path)

#parse_file("Common.ui")

parse_all_ui_files()

convert_field_sets_to_lists()
with open("out.json", "w") as file:
    file.write(json.dumps(data, indent=4))

import gen_docs