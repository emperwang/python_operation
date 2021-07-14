#!/usr/bin/python3
# coding=utf-8

import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("analyse.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element :%s" % collection.getAttribute("shelf"))

# get all movie
moveis = collection.getElementsByTagName("movie")

# print movie info
for move in moveis:
    print("***Movie***")
    if move.hasAttribute("title"):
        print("Title :%s" % move.getAttribute("title"))

    type = move.getElementsByTagName('type')[0]
    print("Type: %s" % type.childNodes[0].data)
    format = move.getElementsByTagName('format')[0]
    print("Format: %s" % format.childNodes[0].data)
    rating = move.getElementsByTagName('rating')[0]
    print("Rating:%s" % rating.childNodes[0].data)
    description = move.getElementsByTagName('description')[0]
    print("Description: %s" % description.childNodes[0].data)


