from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Museo
import urllib.parse
import urllib.request

from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys

#Clase para parsear el xml y crear la base de datos.
class myContentHandler(ContentHandler):

    def __init__ (self):
        self.inItem = False
        self.inContent = False
        self.theContent = ""
        self.atributos = ""

    def startElement (self, name, attrs):
        if name == 'contenido':
            self.inItem = True
        elif self.inItem:
            if name == 'atributo':
                self.inContent = True
            elif name == 'link':
                self.inContent = True

    def endElement (self, name):
        global atributos

        if name == 'item':
            self.inItem = False
        elif self.inItem:
            if name == 'atributo':
                line = "atributo: " + self.theContent + "."
                self.atributos = self.theContent
                # To avoid Unicode trouble
                #print line.encode('utf-8')
                self.inContent = False
                self.theContent = ""
                #print(self.nombre)


    def characters (self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars

xmlFile = urllib.request.urlopen('https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full')

theParser = make_parser()
theHandler = myContentHandler()
theParser.setContentHandler(theHandler)

theParser.parse(xmlFile)
