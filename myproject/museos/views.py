# From https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/
from django.shortcuts import render, render_to_response, redirect

from .models import Museo, Usuario, Comentario, Favorito

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

# From https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
from django.db.models import Count

from math import ceil
from museos.parser import XML_parser

atributos = []

def get_formato(request):
    if request.user.is_authenticated():
        user = request.user.username
    else:
        return ""

    usuario = Usuario.objects.get(nombre=user)

    # From https://www.w3schools.com/tags/tag_style.asp
    formato  = ("body{font-family: 'georgia', 'times new roman', serif;"
                "font-size: " + usuario.letra + "em;"
                "background-color: " + usuario.color + ";}")

    return formato

# Página principal "/"
def home(request, d1=0, d2=5):
    museos_totales = Museo.objects.all()
    # Compruebo si está selecccionado el botón de accesibles
    if request.method == "GET" and 'Accesible' in request.GET:
        if request.GET['Accesible'] != "":
            accesible = request.GET["Accesible"]
            museos = Museo.objects.filter(ACCESIBILIDAD=accesible)
        else:
            return HttpResponseNotFound ("No hay museos accesibles")

        return render_to_response('web/inicio.html', {'Titulo': 'Listado de museos',
            'museos': museos, 'paginas': Usuario.objects.all(),
            'accesible': accesible, 'formato': get_formato(request)},
            context_instance=RequestContext(request))

    # Si no está seleccionado muestro los 5 museos
    #From https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
    museos = Museo.objects.annotate(count=Count('comentario__museo')).order_by('-count').annotate()[int(d1):int(d2)]

    # Escribo las páginas con museos
    accesible = 0
    j = 1
    pages = ""
    for i in range(0,int(ceil(museos_totales.count()/5))):
        pages += "<a href='http://localhost:8000/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    return render_to_response('web/inicio.html', {'Titulo': 'Inicio',
        'museos': museos, 'pages': pages, 'paginas': Usuario.objects.all(),
        'accesible': accesible, 'formato': get_formato(request)},
        context_instance=RequestContext(request))


# Descargo el xml de la página
def get_bd(request):

    #xml = urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full")
    #return HttpResponse(xml, content_type='text/xml')
    museos = XML_parser(XML_File=urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full"))

    for museo in museos:
        try:
            id_entidad = museos[museo]['ID-ENTIDAD']
        except KeyError:
            id_entidad = "No disponible"
        try:
            nombre = museos[museo]['NOMBRE']
        except KeyError:
            nombre = "No disponible"
        try:
            descripcion = museos[museo]['DESCRIPCION']
        except KeyError:
            descripcion = "No disponible"
        try:
            horario = museos[museo]['HORARIO']
        except KeyError:
            horario = "No disponible"
        try:
            transporte = museos[museo]['TRANSPORTE']
        except KeyError:
            transporte = "No disponible"
        try:
            accesibilidad = museos[museo]['ACCESIBILIDAD']
        except KeyError:
            accesibilidad = "No disponible"
        try:
            url = museos[museo]['CONTENT-URL']
        except KeyError:
            url = "No disponible"
        try:
            nombre_via = museos[museo]['NOMBRE-VIA']
        except KeyError:
            nombre_via = "No disponible"
        try:
            clase_vial = museos[museo]['CLASE-VIAL']
        except KeyError:
            clase_vial = "No disponible"
        try:
            tipo_num = museos[museo]['TIPO-NUM']
        except KeyError:
            tipo_num = "No disponible"
        try:
            num = museos[museo]['NUM']
        except KeyError:
            num = "No disponible"
        try:
            localidad = museos[museo]['LOCALIDAD']
        except KeyError:
            localidad = "No disponible"
        try:
            provincia = museos[museo]['PROVINCIA']
        except KeyError:
            provincia = "No disponible"
        try:
            cp = museos[museo]['CODIGO-POSTAL']
        except KeyError:
            cp = "No disponible"
        try:
            barrio = museos[museo]['BARRIO']
        except KeyError:
            barrio = "No disponible"
        try:
            distrito = museos[museo]['DISTRITO']
        except KeyError:
            distrito = "No disponible"
        try:
            cx = museos[museo]['COORDENADA-X']
        except KeyError:
            cx = "No disponible"
        try:
            cy = museos[museo]['COORDENADA-Y']
        except KeyError:
            cy = "No disponible"
        try:
            latitud = museos[museo]['LATITUD']
        except KeyError:
            latitud = "No disponible"
        try:
            longitud = museos[museo]['LONGITUD']
        except KeyError:
            longitud = "No disponible"
        try:
            tlf = museos[museo]['TELEFONO']
        except KeyError:
            tlf = "No disponible"
        try:
            fax = museos[museo]['FAX']
        except KeyError:
            fax = "No disponible"
        try:
            email = museos[museo]['EMAIL']
        except KeyError:
            email = "No disponible"

        m = Museo(ID_ENTIDAD=id_entidad, NOMBRE=nombre, DESCRIPCION=descripcion,
            HORARIO=horario, TRANSPORTE=transporte, ACCESIBILIDAD=accesibilidad,
            CONTENT_URL=url, NOMBRE_VIA=nombre_via, CLASE_VIAL=clase_vial,
            TIPO_NUM=tipo_num, NUM=num, LOCALIDAD=localidad, PROVINCIA=provincia,
            CODIGO_POSTAL = cp, BARRIO=barrio, DISTRITO=distrito,
            COORDENADA_X=cx, COORDENADA_Y=cy, LATITUD = latitud,
            LONGITUD= longitud, TELEFONO=tlf, FAX=fax, EMAIL=email)
        m.save()

    return redirect("/")

# Muestro el listado de museos
def listar(request):
    distritos = Museo.objects.values('DISTRITO').distinct()
    lista = []
    Dist_select = "Elige un distrito"
    for distrito in distritos:
        lista.append(str(distrito).split(':')[1][2:-2])

    # Compruebo si hay búsqueda de distrito
    if request.method == "GET" and 'Distrito' in request.GET:
        if request.GET['Distrito'] != "":
            Dist_select = request.GET['Distrito']
            museos = Museo.objects.filter(DISTRITO=str(request.GET["Distrito"]))
        else:
            return HttpResponseNotFound ("No hay museos en ese distrito")

    # Si no la hay muestro todos los museos
    else:
        museos = Museo.objects.all()

        #return HttpResponse(lista)
    return render_to_response('web/museos.html', {'Titulo': 'Listado de museos',
        'museos': museos, 'formato': get_formato(request),
        'distritos': lista, 'Dist_select': Dist_select},
        context_instance=RequestContext(request))


# Muestro los datos del museo
@csrf_exempt
def mostrar_museo(request, id):
    add = ""
    # Compruebo si el museo existe
    try:
        museo = Museo.objects.get(id=id)
    except Museo.DoesNotExist:
        return HttpResponseNotFound("El museo no existe.")

    # Compruebo si se ha rellenado algún formulario
    if request.method == "POST":
        usuario = request.user.username
        try:
            usuario = Usuario.objects.get(nombre=usuario)
        except Usuario.DoesNotExist:
            return HttpResponseNotFound("Debes estar logueado.")

        #Compruebo si han añadido un comentario
        if 'Comentario' in request.POST:
            if request.POST["Comentario"] != "":
                comentario = Comentario(texto=request.POST["Comentario"],
                    museo=Museo.objects.get(id=id))
                comentario.save()

        #Compruebo si el museo está añadido a favoritos
        elif 'Add' in request.POST:
            for favorito in  Museo.objects.filter(favorito__usuario=usuario):
                if favorito == Museo.objects.get(id=id):
                    return HttpResponseNotFound("El museo ya está añadido")

            f = Favorito(museo=Museo.objects.get(id=id), usuario=usuario)
            f.save()
            add = "Museo añadido."

    comentarios = Comentario.objects.filter(museo=Museo.objects.get(id=id))

    return render_to_response('web/museo.html', {'Titulo': 'Ficha técnica',
        'museo': Museo.objects.get(id=id), 'add': add, 'formato': get_formato(request),
        'comentarios': comentarios}, context_instance=RequestContext(request))


# Muestro los datos del usuario
def usuario(request, usuario, d1=0, d2=5):
    try:
        # Extraigo el usuario del URL
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    # Actualizo el valor del formulario
    if request.method == "POST" and request.user.is_authenticated():
        if 'Titulo' in request.POST:
            usuario.titulo = request.POST['Titulo']
        elif 'Letra' in request.POST and 'Color' in request.POST:
            usuario.letra = request.POST['Letra']
            usuario.color = request.POST['Color']

        usuario.save()

    # Muestro los museos de la página que corresponde
    # From https://stackoverflow.com/questions/1981524/django-filtering-on-foreign-key-properties
    museos = Museo.objects.filter(favorito__usuario=usuario).annotate()[int(d1):int(d2)]
    favoritos = Favorito.objects.filter(usuario=usuario)

    # Escribo las páginas con museos
    j = 1
    pages = ""
    for i in range(0,int(ceil(Favorito.objects.filter(usuario=usuario).count()/5))):
        pages += "<a href='http://localhost:8000/" + str(usuario.nombre) + "/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    if usuario.titulo == "":
        return render_to_response('web/usuario.html', {'Titulo': "Página de " + usuario.nombre,
            'usuario': usuario, 'museos': museos, 'pages': pages, 'formato': get_formato(request),
            'favoritos': favoritos}, context_instance=RequestContext(request))
    else:
        return render_to_response('web/usuario.html', {'Titulo': usuario.titulo,
            'usuario': usuario, 'museos': museos, 'pages': pages, 'formato': get_formato(request),
            'favoritos': favoritos}, context_instance=RequestContext(request))


# Muestro el xml del usuario
def mostrar_xml(request, usuario):
    try:
        usuario = Usuario.objects.get(nombre = usuario)
    except Usuario.DoesNotExist:
        return HttpResponseNotFound("Usuario inexistente.")

    return render_to_response('xml/xml_tmp.xml', {'nombre': str(usuario.nombre),
    'museos': Museo.objects.filter(favorito__usuario=usuario)}, content_type='text/xml')

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
