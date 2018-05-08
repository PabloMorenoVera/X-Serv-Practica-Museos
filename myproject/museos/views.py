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

from django.utils.datastructures import MultiValueDictKeyError

#Función para comprobar si un usuario está logueado
def auth(request):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.' + "<a href='/login'>Login</a>"
    return logged

# Tengo que meter el value del hidden en la plantilla como una variable.
form_accesibilidad = """
<form action="" method="GET">
    <input type="hidden" name="Accesible" value="1">
    <input type="submit" value="Accesibles">
</form>
"""

def mostrar_accesibles():
    respuesta = "<ul>"
    for listado in Museo.objects.filter(accesibilidad=1):
        respuesta += "<li><a href= '" + str(listado.url) + "'>" + listado.nombre + '</a>'
    respuesta += "</ul>"
    logged = auth(request)
    return HttpResponse(form_accesibilidad + logged + "<br><br><h1>Listado de Museos accesibles</h1>" + respuesta)


#Página principal "/"
def home(request, d1 = 0, d2 = 5):
    respuesta = "<ul>"
    if request.path == "/":
        #Compruebo si está selecccionado el botón de accesibles
        try:
            accesible = request.GET["Accesible"]
            museos_accesibles = Museo.objects.filter(accesibilidad=accesible)
            if str(museos_accesibles) == "[]":
                return HttpResponseNotFound (form_accesibilidad + "No hay museos accesibles")

            for listado in museos_accesibles:
                respuesta += "<li><a href='" + str(listado.url) + "'>" + listado.nombre + '</a>'

        #Si no está seleccionado muestro los 5 primeros museos
        except MultiValueDictKeyError:
            for listado in Museo.objects.all()[:5]:
                respuesta += "<li><a href= '" + str(listado.url) + "'>" + listado.nombre + '</a>'

    else:
        #Muestro los museos de la página que corresponde
        for listado in Museo.objects.all()[int(d1):int(d2)]:
            respuesta += "<li><a href= '" + str(listado.url) + "'>" + listado.nombre + '</a>'

    respuesta += "</ul>"

    #Escribo las páginas con museos
    j = 1
    for i in range(0,int(round(Museo.objects.all().count()/5,0)+1)):
        respuesta += "<a href='http://localhost:8000/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    #Añado la autenticación
    logged = auth(request)
    return HttpResponse(form_accesibilidad + logged + "<br><br><h1>Listado de Museos</h1>" + respuesta)

#Descargo el xml de la página
def get_xml(request):
    xml = urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
    return HttpResponse(xml, content_type='text/xml')


formulario = """
<form action="" method="GET">
    <input type="text" name="Distrito" value=""><br>
    <input type="submit" value="Enviar">
</form>
"""

# Muestro el listado de museos o usuarios
def listar(request):
    respuesta = "<title>Práctica museos</title>"

    #listo los museos
    if request.path == "/museos":
        respuesta += formulario
        respuesta += "<h1>Listado de museos<br></h1>"
        respuesta += "<ul>"

        #Compruebo si hay búsqueda de distrito
        try:
            distrito = request.GET["Distrito"]
            museos_distrito = Museo.objects.filter(distrito=str(distrito))
            if str(museos_distrito) == "[]":
                return HttpResponseNotFound (formulario + "No hay museos en ese distrito")
            for listado in museos_distrito:
                respuesta += "<li><a href='" + str(listado.url) + "'>" + listado.nombre + '</a>'

        #Si no la hay muestro todos los museos
        except MultiValueDictKeyError:
            for listado in Museo.objects.all():
                respuesta += "<li><a href='" + str(listado.url) + "'>" + listado.nombre + '</a>'

        respuesta += "</ul>"

    #Listo los usuarios
    elif request.path == "/usuarios":
        respuesta += "<h1>Listado de usuarios<br></h1>"
        for listado in Usuario.objects.all():
            respuesta += "<li>" + str(listado.nombre)
        respuesta += "</ul>"
    else:
        return HttpResponseNotFound("Recurso inexistente.")

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

#Muestro el xml del usuario
def mostrar_xml(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    tmp = get_template("xml/xml_tmp.xml")
    c = Context({'nombre': str(usuario.nombre), 'museos': usuario.museos.all()})
    return HttpResponse(tmp.render(c), content_type='text/xml')
