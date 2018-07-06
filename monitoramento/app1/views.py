# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.gis.geos import Point
from app1.models import PontosColeta, Consulta
from django.core.serializers import serialize
from django.db import connection, transaction
from .forms import saneform
from app1.models import sane
from django.contrib.gis.geos import GEOSGeometry
import json

# Create your views here.
def retorna_geodjason(request):

    opt=request.GET['consulta_tema']

    #print opt;

    #print PontosColeta.objects.all()
    cursor = connection.cursor()
    cursor.execute("drop table IF EXISTS app1_consulta ;")
    #cursor.execute("create table consulta as select cpf_cnpj as id,cpf_cnpj , geom, nome_empresa, sum(valor) from despesas where valor is not NULL and ds_funcao = '%s' and data >= '%s' and data >= '%s' group by cpf_cnpj, nome_empresa,geom" % (opt,di,df))
    #cursor.execute("CREATE table SELECT capitais_ponto.* FROM capitais_ponto WHERE capitais_ponto.regiao='%s'" % (opt))
    cursor.execute("CREATE table app1_consulta AS SELECT * FROM pontos_coleta WHERE pontos_coleta.pt_id='%s'" % (opt))

    geoj = serialize('geojson', Consulta.objects.all())
    #print geoj
    # geoj = serialize('geojson',geoj)

    return HttpResponse(geoj, content_type='json')

def index(request):
    return render(request, 'app1/index.html', {})

def projeto(request):
    return render(request, 'app1/projeto.html', {})

def levantamentos(request):
    return render(request, 'app1/levantamentos.html', {})

def planilha2018(request):
    return render(request, 'app1/Plan_Coleta_Dados.html', {})

def planilha2017(request):
    return render(request, 'app1/saneamento_v2.html', {})



def apresenta(request):
    img = sane.objects.all() #########################  requisita todos as linhas da tabela dogs do banco de dados
    return render(request, 'app1/apresenta.html',{'img': img} ) ######################### retorna a pagina apresenta.html e passa como parametros todas as linhas da tabela dogs do banco de dados


def site(request):

    form = saneform ######################### cria uma nova instancia do formulario dogform
    return render(request, 'app1/projeto.html',{'form': form} ) ######################### retorna a pagina main.html e passa como parametro o formulario dogform

def addponto(request):

    if request.method == 'POST': ######################## verifica se a requisição utiliza o método http POST
        form = saneform(request.POST, request.FILES) ######################## cria uma instancia do formulário dogform com as informações passadas pelo no request que veio das paginas html,

        if form.is_valid():  ######################## verifico se o formulario instaciado é valido
            form.save() ######################## salvo o formulario no banco

        else:
            print form.errors ######################## se ocorrer algum erro é printado

    return render(request, 'app1/projeto.html', {'form': form}) ######################## apos adicionado o objeto é retonado a mesma pagina com o formulario
