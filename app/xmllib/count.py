import xml.sax


class XmlHandlerCount(xml.sax.ContentHandler):
    result = 0

    def startElement(self, name, attributes):
        if name == "item":
            self.result = self.result + 1


def product_count(file_name: str) -> int:
    handler = XmlHandlerCount()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    with open(file_name, "r") as xml_file:
        parser.parse(xml_file)

    return handler.result
