# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.gis.geos import Point
from app1.models import CapitaisPonto, App1Consulta
from django.core.serializers import serialize
from django.db import connection, transaction


import json

# Create your views here.
def retorna_geodjason(request):

    opt=request.GET['consulta_tema']
    print "ta rolando"
    # geoj = serialize('geojson', json.dumps(Despesas.objects.filter( data__gt=datetime.strptime(di, '%Y-%m-%d'), data__lt=datetime.strptime(df , '%Y-%m-%d'), ds_funcao=opt ).values('nome_empresa','cpf_cnpj','valor','geom').annotate(Sum('valor')), ensure_ascii=False) )
    # # sql =("SELECT nome_empresa, cpf_cnpj as id, sum(valor) FROM despesas where ds_funcao = '%s' group by cpf_cnpj, nome_empresa;" % ('SANEAMENTO'))
    # sql ="SELECT nome_empresa, cpf_cnpj AS id FROM despesas where ds_funcao ='SAUDE' "
    # geoj = serialize('geojson', Despesas.objects.raw(sql),fields=('geom',))

    print CapitaisPonto.objects.all()
    cursor = connection.cursor()
    cursor.execute("drop table IF EXISTS app1_consulta ;")
    #cursor.execute("create table consulta as select cpf_cnpj as id,cpf_cnpj , geom, nome_empresa, sum(valor) from despesas where valor is not NULL and ds_funcao = '%s' and data >= '%s' and data >= '%s' group by cpf_cnpj, nome_empresa,geom" % (opt,di,df))
    #cursor.execute("CREATE table SELECT capitais_ponto.* FROM capitais_ponto WHERE capitais_ponto.regiao='%s'" % (opt))
    cursor.execute("CREATE table app1_consulta AS SELECT * FROM capitais_ponto WHERE capitais_ponto.regiao='norte'")

    geoj = serialize('geojson', App1Consulta.objects.all())
    print geoj
    # geoj = serialize('geojson',geoj)


    return HttpResponse(geoj, content_type='json')

def site(request):
    return render(request,'app1/index.html',{})
