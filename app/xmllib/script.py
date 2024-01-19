import xml.sax

import logging

# counter = 0

# class XmlHandler(xml.sax.ContentHandler):
#     counter = 0

#     def startDocument(self) -> None:
#        print( "Running...")

#     def endDocument(self) -> None:
#        print( "done.")

#     def startElement(self, name, attributes):
#         if name == "item":
#             self.counter = self.counter + 1
#             print( attributes["name"])
#         # if name == "categoriesWithParts":
#         #     print(attributes)
#         #     for (k,v) in attributes.items():
#         #         print("\t\t", k, v)

# handler = XmlHandler()
# parser = xml.sax.make_parser()
# parser.setContentHandler(handler)

# with open(file_name, "r") as xml_file:
#     parser.parse(xml_file)

# print(handler.counter)

