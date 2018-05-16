#!/usr/bin/python3

# From https://docs.python.org/2/library/xml.etree.elementtree.html
import xml.etree.ElementTree as ET

def XML_parser(XML_File):
    tree = ET.parse(XML_File)

    contenidos = tree.getroot()

    lista_museos = {}
    for contenido in contenidos:
        for atributos in contenido:
            if atributos.tag == 'atributos':
                museo = {}
                for atributo in atributos:
                    for datos in atributo:
                        museo[datos.attrib['nombre']] = datos.text
                    if not '\n' in atributo.text:
                        museo[atributo.attrib['nombre']] = atributo.text


                lista_museos[museo['ID-ENTIDAD']] = museo

    return lista_museos
