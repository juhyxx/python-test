import xml.sax


def product_list(file_name):
    class XmlHandlerList(xml.sax.ContentHandler):
        data = []

        def startElement(self, name, attributes):
            global text
            if name == "item":
                self.data.append(attributes["name"])

    handler = XmlHandlerList()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    with open(file_name, "r") as xml_file:
        parser.parse(xml_file)

    return handler.data