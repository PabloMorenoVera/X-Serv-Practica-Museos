# From https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/
from django.shortcuts import render, render_to_response, redirect

from .models import Museo, Usuario, Comentario, Favorito

# From https://code.djangoproject.com/ticket/1494 and https://stackoverflow.com/questions/44185354/django-tutorial-name-httpresponse-is-not-defined
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import authenticate, login, logout
# From https://stackoverflow.com/questions/23139657/django-get-all-users
from django.contrib.auth.models import User

from django.template.loader import get_template
# From https://lincolnloop.com/blog/getting-requestcontext-your-templates/
from django.template import Context, RequestContext

import urllib.parse
import urllib.request

from django.utils.datastructures import MultiValueDictKeyError

# From https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
from django.db.models import Count

from math import ceil
from museos.parser import XML_parser

bd = True

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
    global bd

    #Compruebo si están todos los usuario registrados
    users = User.objects.all()
    for user in users:
        try:
            Usuario.objects.get(nombre=user)
        # Si no lo están los añado
        except Usuario.DoesNotExist:
            u = Usuario(nombre=user, letra=1, color="white", titulo="")
            u.save()

    museos_totales = Museo.objects.all()
    # Compruebo si está selecccionado el botón de accesibles
    if request.method == "GET" and 'Accesible' in request.GET:
        if request.GET['Accesible'] != "":
            accesible = request.GET["Accesible"]
            museos = Museo.objects.filter(ACCESIBILIDAD=accesible)
        else:
            return render_to_response('web/error.html', {'Mensaje': "No hay museos accesibles",
                'formato': get_formato(request)}, context_instance=RequestContext(request))

        return render_to_response('web/inicio.html', {'Titulo': 'Listado de museos',
            'museos': museos, 'paginas': Usuario.objects.all(),
            'accesible': accesible, 'formato': get_formato(request), 'bd': bd},
            context_instance=RequestContext(request))

    # Si no está seleccionado muestro los 5 museos
    #From https://docs.djangoproject.com/en/1.8/topics/db/examples/many_to_one/
    museos = Museo.objects.annotate(count=Count('comentario__museo')).order_by('-count')[int(d1):int(d2)]

    # Escribo las páginas con museos
    accesible = 0
    j = 1
    pages = ""
    for i in range(0,int(ceil(museos_totales.count()/5))):
        pages += "<a href='http://localhost:8000/" + str(i*5) + "-" + str(i*5+5) + "'>" + str(j) + "</a> "
        j += 1

    return render_to_response('web/inicio.html', {'Titulo': 'Inicio',
        'museos': museos, 'pages': pages, 'paginas': Usuario.objects.all(),
        'accesible': accesible, 'formato': get_formato(request), 'bd': bd},
        context_instance=RequestContext(request))


# Descargo el xml de la página
def get_bd(request):
    global bd
    museos = XML_parser(XML_File=urllib.request.urlopen("https://datos.madrid.es/portal/site/egob/menuitem.ac61933d6ee3c31cae77ae7784f1a5a0/?vgnextoid=00149033f2201410VgnVCM100000171f5a0aRCRD&format=xml&file=0&filename=201132-0-museos&mgmtid=118f2fdbecc63410VgnVCM1000000b205a0aRCRD&preview=full"))

    for museo in museos:
        try:
            id_entidad = museos[museo]['ID-ENTIDAD']
        except KeyError:
            id_entidad = "N/D"
        try:
            nombre = museos[museo]['NOMBRE']
        except KeyError:
            nombre = "N/D"
        try:
            descripcion = museos[museo]['DESCRIPCION']
        except KeyError:
            descripcion = "N/D"
        try:
            horario = museos[museo]['HORARIO']
        except KeyError:
            horario = "N/D"
        try:
            transporte = museos[museo]['TRANSPORTE']
        except KeyError:
            transporte = "N/D"
        try:
            accesibilidad = museos[museo]['ACCESIBILIDAD']
        except KeyError:
            accesibilidad = "N/D"
        try:
            url = museos[museo]['CONTENT-URL']
        except KeyError:
            url = "N/D"
        try:
            nombre_via = museos[museo]['NOMBRE-VIA']
        except KeyError:
            nombre_via = "N/D"
        try:
            clase_vial = museos[museo]['CLASE-VIAL']
        except KeyError:
            clase_vial = "N/D"
        try:
            tipo_num = museos[museo]['TIPO-NUM']
        except KeyError:
            tipo_num = "N/D"
        try:
            num = museos[museo]['NUM']
        except KeyError:
            num = "N/D"
        try:
            localidad = museos[museo]['LOCALIDAD']
        except KeyError:
            localidad = "N/D"
        try:
            provincia = museos[museo]['PROVINCIA']
        except KeyError:
            provincia = "N/D"
        try:
            cp = museos[museo]['CODIGO-POSTAL']
        except KeyError:
            cp = "N/D"
        try:
            barrio = museos[museo]['BARRIO']
        except KeyError:
            barrio = "N/D"
        try:
            distrito = museos[museo]['DISTRITO']
        except KeyError:
            distrito = "N/D"
        try:
            cx = museos[museo]['COORDENADA-X']
        except KeyError:
            cx = "N/D"
        try:
            cy = museos[museo]['COORDENADA-Y']
        except KeyError:
            cy = "N/D"
        try:
            latitud = museos[museo]['LATITUD']
        except KeyError:
            latitud = "N/D"
        try:
            longitud = museos[museo]['LONGITUD']
        except KeyError:
            longitud = "N/D"
        try:
            tlf = museos[museo]['TELEFONO']
        except KeyError:
            tlf = "N/D"
        try:
            fax = museos[museo]['FAX']
        except KeyError:
            fax = "N/D"
        try:
            email = museos[museo]['EMAIL']
        except KeyError:
            email = "N/D"

        m = Museo(ID_ENTIDAD=id_entidad, NOMBRE=nombre, DESCRIPCION=descripcion,
            HORARIO=horario, TRANSPORTE=transporte, ACCESIBILIDAD=accesibilidad,
            CONTENT_URL=url, NOMBRE_VIA=nombre_via, CLASE_VIAL=clase_vial,
            TIPO_NUM=tipo_num, NUM=num, LOCALIDAD=localidad, PROVINCIA=provincia,
            CODIGO_POSTAL = cp, BARRIO=barrio, DISTRITO=distrito,
            COORDENADA_X=cx, COORDENADA_Y=cy, LATITUD = latitud,
            LONGITUD= longitud, TELEFONO=tlf, FAX=fax, EMAIL=email)
        m.save()

    bd = False
    return redirect("/")

# Muestro el listado de museos
def listar(request):
    distritos = Museo.objects.values('DISTRITO').distinct()
    lista = []
    markers = []
    Dist_select = "Elige un distrito"
    for distrito in distritos:
        lista.append(str(distrito).split(':')[1][2:-2])

    # Compruebo si hay búsqueda de distrito
    if request.method == "GET" and 'Distrito' in request.GET:
        if request.GET['Distrito'] != "":
            Dist_select = request.GET['Distrito']
            museos = Museo.objects.filter(DISTRITO=str(request.GET["Distrito"]))
        else:
            return render_to_response ('web/error.html', {'Mensaje': "No hay museos en ese distrito",
                'formato': get_formato(request)}, context_instance=RequestContext(request))

    # Si no la hay muestro todos los museos
    else:
        museos = list(Museo.objects.all())

        #return HttpResponse(lista)
    return render_to_response('web/museos.html', {'Titulo': 'Listado de museos',
        'museos': museos, 'formato': get_formato(request),'distritos': lista,
        'Dist_select': Dist_select},
        context_instance=RequestContext(request))


# Muestro los datos del museo
@csrf_exempt
def mostrar_museo(request, id):
    add = ""
    # Compruebo si el museo existe
    try:
        museo = Museo.objects.get(id=id)
    except Museo.DoesNotExist:
        return render_to_response ('web/error.html', {'Mensaje': "El museo no existe",
            'formato': get_formato(request)}, context_instance=RequestContext(request))

    # Compruebo si se ha rellenado algún formulario
    if request.method == "POST":
        usuario = request.user.username
        try:
            usuario = Usuario.objects.get(nombre=usuario)
        except Usuario.DoesNotExist:
            return render_to_response ('web/error.html', {'Mensaje': "Debes estar logueado",
                'formato': get_formato(request)}, context_instance=RequestContext(request))

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
                    return render_to_response ('web/error.html', {'Mensaje': "El museo ya está añadido",
                        'formato': get_formato(request)}, context_instance=RequestContext(request))

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
        return HttpResponseNotFound("Error 404. Usuario inexistente.")

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
   # From https://stackoverflow.com/questions/12758786/redirect-return-to-same-previous-page-in-django/12758859
   return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# From https://stackoverflow.com/questions/20208562/homepage-login-form-django
def loginUser(request):
    if request.POST:
        usuario = request.POST['user']
        contraseña = request.POST['psswd']
        user = authenticate(username=usuario, password=contraseña)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return render_to_response ('web/error.html', {'Mensaje': "Usuario Incorrecto",
                'formato': get_formato(request)}, context_instance=RequestContext(request))

def about(request):
    return render_to_response('web/about.html', {'Titulo': "About", 'formato': get_formato(request)},
        context_instance=RequestContext(request))
