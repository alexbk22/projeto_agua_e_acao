# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.gis.geos import Point
from app1.models import PontosColeta, Consulta
from django.core.serializers import serialize
from django.db import connection, transaction

import json

# Create your views here.
def retorna_geodjason(request):

    opt=request.GET['consulta_tema']
    print opt;
    #print PontosColeta.objects.all()
    cursor = connection.cursor()
    cursor.execute("drop table IF EXISTS app1_consulta ;")
    #cursor.execute("create table consulta as select cpf_cnpj as id,cpf_cnpj , geom, nome_empresa, sum(valor) from despesas where valor is not NULL and ds_funcao = '%s' and data >= '%s' and data >= '%s' group by cpf_cnpj, nome_empresa,geom" % (opt,di,df))
    #cursor.execute("CREATE table SELECT capitais_ponto.* FROM capitais_ponto WHERE capitais_ponto.regiao='%s'" % (opt))
    cursor.execute("CREATE table app1_consulta AS SELECT * FROM pontos_coleta WHERE pontos_coleta.pt_id='%s'" % (opt))

    geoj = serialize('geojson', Consulta.objects.all())
    print geoj
    # geoj = serialize('geojson',geoj)

    return HttpResponse(geoj, content_type='json')

def site(request):
    return render(request, 'app1/index.html', {})
