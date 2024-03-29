import xml.sax


class XmlHandlerList(xml.sax.ContentHandler):
    result = []

    def startElement(self, name, attributes):
        global text
        if name == "item":
            self.result.append(attributes["name"])


def product_list(file_name: str) -> int:
    handler = XmlHandlerList()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    with open(file_name, "r") as xml_file:
        parser.parse(xml_file)

    return handler.result
