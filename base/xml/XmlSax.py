#!/usr/bin/python3
# coding=utf-8

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'movie':
            print("***************Movie****************")
            title = attributes['title']
            print("Title:", title)

    def endElement(self, tag):
        if self.CurrentData == 'type':
            print("Type :", self.type)
        elif self.CurrentData == 'format':
            print("Format :", self.format)
        elif self.CurrentData == 'year':
            print("Year :", self.year)
        elif self.CurrentData == 'rating':
            print("Rating: ",self.rating)
        elif self.CurrentData == 'stars':
            print("Stars :",self.stars)
        elif self.CurrentData == 'description':
            print("Description:", self.description)
        self.CurrentData = "";

    def characters(self, content):
        if self.CurrentData == 'type':
            self.type = content
        elif self.CurrentData == 'format':
            self.format = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'rating':
            self.rating = content
        elif self.CurrentData == 'stars':
            self.stars = content
        elif self.CurrentData == 'description':
            self.description = content

if __name__ == "__main__":
    # create XML Reader
    parser = xml.sax.make_parser();
    # close namespace
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # rewrite handler
    handler = MovieHandler()
    parser.setContentHandler(handler)

    parser.parse("analyse.xml")