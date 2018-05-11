"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.auth.views import login
from django.views.static import serve

urlpatterns = [
    url(r'media/(.*)$', serve, {'document_root': 'templates/web'}),
    url(r'^$', 'museos.views.home'),
    url(r'^(\d+)-(\d+)', 'museos.views.home'),
    # From https://stackoverflow.com/questions/25274104/logout-page-not-working-in-django
    url(r'^logout', 'museos.views.logoutUser'),
    url(r'^login', 'museos.views.loginUser'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xml$', 'museos.views.get_xml'),
    url(r'^museos$', 'museos.views.listar'),
    url(r'^museos/(\d+)$', 'museos.views.mostrar_museo'),
    url(r'^(\w+)$', 'museos.views.usuario'),
    url(r'^(\w+)/xml$', 'museos.views.mostrar_xml')
]
