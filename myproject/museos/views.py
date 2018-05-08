from django.shortcuts import render

# Create your views here.
from .models import Museo, Usuario, Comentario

from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.template.loader import get_template
from django.template import Context

import urllib.parse
import urllib.request


### Entry.objects.all().filter(pub_date__year=2006)
##  Entry.objects.all()[:5]
##  Entry.objects.all()[5:10]

#Función para comprobar si un usuario está logueado
def auth(request):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
    return logged


#Página principal "/"
def home(request, d1 = 0, d2 = 5):
    respuesta = "<ul>"
    if request.path == "/":
        for listado in Museo.objects.all()[:5]:
            respuesta += "<li><a href= '" + str(listado.url) + "'>" + listado.nombre + '</a>'

    else:
        if Museo.objects.all().count() < int(d1):
            return HttpResponseNotFound("No hay más museos")
        elif Museo.objects.all().count() < int(d2):
            d2 = Museo.objects.all().count()

        for listado in Museo.objects.all()[int(d1):int(d2)]:
            respuesta += "<li><a href= '" + str(listado.url) + "'>" + listado.nombre + '</a>'

    respuesta += "</ul>"

    j = 1
    for i in range(0,int(round(Museo.objects.all().count()/5,0)+1)):
        respuesta += "<a href='http://localhost:8000/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    logged = auth(request)
    return HttpResponse(logged + "<br><br><h1>Listado de Museos</h1>" + respuesta)


def get_xml(request):
    xml = urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
    return HttpResponse(xml, content_type='text/xml')


# Muestro el listado de museos o usuarios
def listar(request):
    respuesta = "<title>Práctica museos</title>"

    #listo los museos
    if request.path == "/museos":
        respuesta += "<h1>Listado de museos<br></h1>"
        respuesta += "<ul>"
        for listado in Museo.objects.all():
            respuesta += "<li><a href='" + str(listado.url) + "'>" + listado.nombre + '</a>'
    #Listo los usuarios
    elif request.path == "/usuarios":
        respuesta += "<h1>Listado de usuarios<br></h1>"
        for listado in Usuario.objects.all():
            respuesta += "<li>" + str(listado.nombre)
    else:
        return HttpResponseNotFound("Recurso inexistente.")

    respuesta += "<ul>"
    logged = auth(request)
    return HttpResponse(logged + respuesta)


#Muestro los datos del museo
def mostrar_museo(request, id):
    try:
        museo = Museo.objects.get(id=id)
    except Museo.DoesNotExist:
        return HttpResponseNotFound("El museo no existe.")

    respuesta = "<title>Práctica museos</title>"
    respuesta += "<h1>Página del museo " + str(museo.nombre) + ".</h1>"
    respuesta += "<head>Distrito:<ul><li>" + str(museo.distrito) + "</ul></head><br>"
    respuesta += "<body>Link: <a href='" + str(museo.url) + "'>" + str(museo.url) + "</a></body>"
    logged = auth(request)
    return HttpResponse(logged + respuesta)


#Muestro los datos del usuario
def usuario(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    respuesta = "<title>Práctica museos</title>"
    respuesta += "<h1>Página personal de " + str(usuario.nombre) + ".</h1>"
    respuesta += "<head>Museos favoritos:<ul>"
    for museo in usuario.museos.all():
        respuesta += "<li>" + str(museo)
    respuesta += "</ul></head><body>Letra: " + str(usuario.letra)
    respuesta += "<br>Color: " + str(usuario.color) + "</body>"
    return HttpResponse(respuesta)

def mostrar_xml(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    tmp = get_template("xml/xml_tmp.xml")
    c = Context({'nombre': str(usuario.nombre), 'museos': usuario.museos.all()})
    return HttpResponse(tmp.render(c), content_type='text/xml')
