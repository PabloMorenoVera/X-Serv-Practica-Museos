# From https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/
from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import Museo, Usuario, Comentario

# From https://code.djangoproject.com/ticket/1494 and https://stackoverflow.com/questions/44185354/django-tutorial-name-httpresponse-is-not-defined
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from django.template.loader import get_template
from django.template import Context
# From https://lincolnloop.com/blog/getting-requestcontext-your-templates/
from django.template import RequestContext

import urllib.parse
import urllib.request

from django.utils.datastructures import MultiValueDictKeyError

atributos = []

# Función para comprobar si un usuario está logueado
def auth(request):
    if request.user.is_authenticated():
        logged = 'Logged in as ' + request.user.username + "    " + "<a href= '/logout'>Logout</a>"
    else:
        logged = 'Not logged in.'
    return logged


# Tengo que meter el value del hidden en la plantilla como una variable.
form_accesibilidad = """
<form action="" method="GET">
    <input type="hidden" name="Accesible" value="1">
    <input type="submit" value="Accesibles">
</form>
"""

# Página principal "/"
def home(request, d1 = 0, d2 = 5):
    museos_totales = Museo.objects.all()
    if request.path == "/":
        # Compruebo si está selecccionado el botón de accesibles
        try:
            accesible = request.GET["Accesible"]
            museos = Museo.objects.filter(accesibilidad=accesible)

            if str(museos) == "[]":
                return HttpResponseNotFound ("No hay museos accesibles")
            else:
                return render_to_response('web/index.html', {'Titulo': 'Listado de museos',
                    'museos': museos, 'logged': auth(request),
                    'paginas': Usuario.objects.all()})

        # Si no está seleccionado muestro los 5 primeros museos
        except MultiValueDictKeyError:
            museos = Museo.objects.annotate()[:5]

    else:
        # Muestro los museos de la página que corresponde
        museos = Museo.objects.annotate()[int(d1):int(d2)]

    # Escribo las páginas con museos
    j = 1
    pages = ""
    for i in range(0,int(round(museos_totales.count()/5,0)+1)):
        pages += "<a href='http://localhost:8000/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    return render_to_response('web/inicio.html', {'Titulo': 'Inicio',
        'museos': museos, 'pages': pages, 'logged': auth(request),
        'paginas': Usuario.objects.all()},
        context_instance=RequestContext(request))


# Descargo el xml de la página
def get_xml(request):
    xml = urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
    return HttpResponse(xml, content_type='text/xml')


formulario = """
<form action="" method="GET">
    <input type="text" name="Distrito" value=""><br>
    <input type="submit" value="Enviar">
</form>
"""

# Muestro el listado de museos
def listar(request):

    # Compruebo si hay búsqueda de distrito
    try:
        distrito = request.GET["Distrito"]
        museos = Museo.objects.filter(distrito=str(distrito))
        if str(lista) == "[]":
            return HttpResponseNotFound (formulario + "No hay museos en ese distrito")

    # Si no la hay muestro todos los museos
    except MultiValueDictKeyError:
        museos = Museo.objects.all()

    return render_to_response('web/museos.html', {'Titulo': 'Listado de museos',
        'museos': museos, 'logged': auth(request)})


# Muestro los datos del museo
def mostrar_museo(request, id):
    try:
        museo = Museo.objects.get(id=id)
    except Museo.DoesNotExist:
        return HttpResponseNotFound("El museo no existe.")

    return render_to_response('web/museo.html', {'Titulo': 'Ficha técnica','museo': museo})

    respuesta = "<title>Práctica museos</title>"
    respuesta += "<h1>Página del museo " + str(museo.nombre) + ".</h1>"
    respuesta += "<head>Distrito:<ul><li>" + str(museo.distrito) + "</ul></head><br>"
    respuesta += "<body>Link: <a href='" + str(museo.url) + "'>" + str(museo.url) + "</a></body>"
    logged = auth(request)
    return HttpResponse(logged + respuesta)


# Muestro los datos del usuario
def usuario(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    return render_to_response('web/usuario.html', {'Titulo': usuario.titulo,
        'usuario': usuario, 'museos': usuario.museos.all(), 'logged': auth(request)})


# Muestro el xml del usuario
def mostrar_xml(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    return render_to_response('xml/xml_tmp.xml', {'nombre': str(usuario.nombre), 'museos': usuario.museos.all()}, content_type='text/xml')

# From https://stackoverflow.com/questions/25274104/logout-page-not-working-in-django
def logoutUser(request):
   logout(request)
   return HttpResponseRedirect('/')

# From https://stackoverflow.com/questions/20208562/homepage-login-form-django
def loginUser(request):
    if request.POST:
       usuario = request.POST['user']
       contraseña = request.POST['psswd']
       user = authenticate(username=usuario, password=contraseña)
       if user is not None:
           login(request, user)
           return HttpResponseRedirect('/')
       else:
           return HttpResponseNotFound("Usuario Incorrecto")
