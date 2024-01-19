
import xml.sax


def product_count(file_name):
    class XmlHandler(xml.sax.ContentHandler):
        counter = 0

        def startElement(self, name, attributes):
            if name == "item":
                self.counter = self.counter + 1

    handler = XmlHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)

    with open(file_name, "r") as xml_file:
        parser.parse(xml_file)

    return handler.counter