import lxml.etree as ET


def parts_list(file_name: str):
    tree = ET.parse(file_name)
    root = tree.getroot()

    parts = root.xpath("//part")
    result = {}
    for part in parts:
        name = part.get("itemName", "Missing name")
        result[name] = []
        for item in part.getchildren():
            result[name].append(item.get("name"))

    return result
