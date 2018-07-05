# -*- coding: utf-8 -*-
from django.db import models ######################## importa a classe model do django
from django.forms import ModelForm ######################## importa a classe modelform do django (para criar formularios direto dos modelos de dados)
from appform.models import sane ######################## importa a classe Dogs do modelo de dados

######################## cria o formulário para inserir dados da coleta
class saneform(ModelForm):
    class Meta:
        model = sane ######################## instancia a classe Dogs
        fields = ('foto','nome_do_ponto','data','periodo','observador','integrantes','od','temperatura','odor','cor','observacoes') ######################## define quais campos do nosso modelo de dados vai compor o formulario

class Apresentform(ModelForm):
    class Meta:
        model = sane
        fields = fields = ('foto','nome_do_ponto','data','periodo','observador','integrantes','od','temperatura','odor','cor','observacoes')
