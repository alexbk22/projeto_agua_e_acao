# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'index', views.site, name='site'),
    url(r'consulta', views.retorna_geodjason),
    url(r'projeto', views.projeto, name='projeto'),
    url(r'levantamentos', views.levantamentos, name='levantamentos'),
    url(r'planilha2018_1', views.planilha2018_1),
    url(r'planilha2017_1', views.planilha2017_1),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
