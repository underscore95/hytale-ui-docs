import os
import re
import json
import shutil

OUT_DIR = "docs"
ROOT_BACK_URL = "https://github.com/underscore95/hytale-ui-docs/tree/main"

with open("out.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def slug(name):
    return re.sub(r"[^a-zA-Z0-9_-]", "-", name)

def link(name, category):
    return f"[{name}]({category}/{slug(name)}.md)"

def back_button(target="Index.md"):
    return f"[← Back]({target})\n\n"

def ensure_dirs():
    if os.path.exists(OUT_DIR):
        shutil.rmtree(OUT_DIR)
    for d in ["ImportedFiles", "Variables", "Types", "UIElements"]:
        os.makedirs(os.path.join(OUT_DIR, d))

def write_index(category, items):
    path = os.path.join(OUT_DIR, f"{category}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(back_button())
        f.write(f"# {category}\n\n")
        for item in sorted(items, key=lambda x: x.get("Name", "")):
            name = item.get("Name", item.get("Alias", ""))
            f.write(f"- {link(name, category)}\n")

def write_imported_files():
    for item in data["ImportedFiles"]:
        name = item["Alias"]
        path = os.path.join(OUT_DIR, "ImportedFiles", f"{slug(name)}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(back_button("../ImportedFiles.md"))
            f.write(f"# {name}\n\n")
            f.write(f"**ImportedFile:** `{item['ImportedFile']}`\n\n")
            f.write(f"**First seen at:** `{item['File']}:{item['LineNumber']}`\n")

def write_variables():
    for item in data["Variables"]:
        name = item["Name"]
        path = os.path.join(OUT_DIR, "Variables", f"{slug(name)}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(back_button("../Variables.md"))
            f.write(f"# {name}\n\n")
            f.write(f"**Defined at:** `{item['File']}:{item['LineNumber']}`\n\n")
            f.write("## Value\n\n")
            f.write("```ui\n")
            f.write(item["Value"])
            f.write("\n```\n")

def write_types():
    for item in data["Types"]:
        name = item["Name"]
        path = os.path.join(OUT_DIR, "Types", f"{slug(name)}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(back_button("../Types.md"))
            f.write(f"# {name}\n\n")
            f.write(f"**First used at:** `{item['File']}:{item['LineNumber']}`\n\n")
            if item["Fields"]:
                f.write("## Fields\n\n")
                for field, info in item["Fields"].items():
                    f.write(f"### {field}\n\n")
                    for v in info["ExampleValues"]:
                        ref = v
                        if isinstance(v, str) and v.startswith("@"):
                            ref = link(v[1:], "Variables")
                        f.write(f"- `{ref}`\n")
                    f.write("\n")

def write_ui_elements():
    for item in data["UIElements"]:
        name = item["Name"]
        path = os.path.join(OUT_DIR, "UIElements", f"{slug(name)}.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(back_button("../UIElements.md"))
            f.write(f"# {name}\n\n")
            f.write(f"**First used at:** `{item['File']}:{item['LineNumber']}`\n\n")
            if "Types" in item:
                f.write("## Uses Types\n\n")
                for t in item["Types"]:
                    f.write(f"- {link(t, 'Types')}\n")

def write_main_index():
    path = os.path.join(OUT_DIR, "Index.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"[← Back]({ROOT_BACK_URL})\n\n")
        f.write("# UI Documentation\n\n")
        f.write("- [Imported Files](ImportedFiles.md)\n")
        f.write("- [Variables](Variables.md)\n")
        f.write("- [Types](Types.md)\n")
        f.write("- [UI Elements](UIElements.md)\n")

def generate_docs():
    ensure_dirs()
    write_index("ImportedFiles", data["ImportedFiles"])
    write_index("Variables", data["Variables"])
    write_index("Types", data["Types"])
    write_index("UIElements", data["UIElements"])
    write_imported_files()
    write_variables()
    write_types()
    write_ui_elements()
    write_main_index()

generate_docs()
