# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'index', views.site, name='site'),
    url(r'consulta', views.retorna_geodjason),
    #url(r'^city/(?P<pk>[0-9]+)$', views.CitiesDetailView.as_view(), name='city-detail'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
