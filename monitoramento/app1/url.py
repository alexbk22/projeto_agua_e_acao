# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'index', views.index),
    url(r'consultajson', views.retorna_geodjason),
    url(r'projeto', views.projeto),
    url(r'levantamentos', views.levantamentos),
    url(r'planilha2018', views.planilha2018),
    url(r'planilha2017', views.planilha2017),
    url(r'addponto', views.addponto),
    url(r'apresenta', views.apresenta),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) ########################## quando usar servidor de desenvolvimento deve-se indicar o local dos uploads aqui
