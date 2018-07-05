# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.gis.db import models  ########################## importa a biblioteca models do modulo gis que contém o tipos de dados normais e espaciais
from django.utils.encoding import python_2_unicode_compatible

# @python_2_unicode_compatible
class sane(models.Model):
    # id = models.AutoField(primary_key=True) ########################## cria um campo do tipo serial e definido com chave primaria da classe
    # ponto = models.CharField(max_length=50) ########################## cria um campo do tipo texto com tamanho máximo de 50 caracteres (char)
    # od= models.CharField(max_length=50)
    # porte = models.CharField(max_length=50)
    # observador = models.CharField(max_length=50)
    # foto = models.ImageField()             ########################## cria um campo do tipo imagem
    # ponto = models.PointField(srid=4326)   ########################## cria um campo do tipo ponto com o sistema de referencia definido com wgs84
        id = models.AutoField(primary_key=True)
        #VARIAVEIS PARA CRIAR LISTA DOS PONTOS DE COLETA CADASTRADOS PREVIAMENTE
        P1 = 'P1'
        P2 = 'P2'
        P3 = 'P3'
        P4 = 'P4'
        P5 = 'P5'
        P6 = 'P6'
        P7 = 'P7'
        P8 = 'P8'
        P9 = 'P9'
        P10 = 'P10'
        #CRIANDO LISTA01
        nome_ponto= (
        (P1, 'P1'),
        (P2, 'P2'),
    	(P3, 'P3'),
    	(P4, 'P4'),
    	(P5, 'P5'),
    	(P6, 'P6'),
        (P7, 'P7'),
        (P8, 'P8'),
        (P9, 'P9'),
        (P10, 'P10'),
                )#DEFINE O VALOR INICIAL
        nome_do_ponto = models.CharField(
            max_length=50,
            choices=nome_ponto, #DEFINE AS ESCOLHAS
            default=P1,       #DEFINE O VALOR INICIAL
        )
        data = models.CharField(max_length=50)
        #VARIAVEIS PARA CRIAR LISTA DE PERIODOS
        M = 'Manha'
        T = 'Tarde'
        N = 'Noite'
        #CRIANDO LISTA02
        periodo= (
    	     (M,'Manha'),
    		 (T,'Tarde'),
    		 (N,'Noite'),
    	         )
        periodo = models.CharField(
    	     max_length=50,
    		 choices=periodo, #DEFINE AS ESCOLHAS
    		 default=M,  #DEFINE O VALOR INICIAL
    		 )
        observador = models.CharField(max_length=50)
        integrantes = models.CharField(max_length=500)
        od = models.CharField(max_length=50)
        temperatura = models.CharField(max_length=50)
        #VARIAVEIS PARA CRIAR LISTA DE ODOR
        Hi = 'Forte'
        Me = 'Medio'
        Lo = 'Fraco'
        No = 'Nenhum'
        #CRIANDO LISTA03
        odor = (
    	       (Hi,'Forte'),
    	       (Me,'Medio'),
    	       (Lo,'Fraco'),
    	       (No,'Nenhum'),
    		   )
        odor = models.CharField(
    	     max_length=50,
    		 choices=odor, #DEFINE AS ESCOLHAS
    		 default=Lo,    #DEFINE O VALOR INICIAL
    		 )
        #VARIAVEIS PARA CRIAR LISTA DE COR
        CZ='Cinza'
        MR='Marrom'
        AM='Amarelada'
        TR='Transparente'
        #CRIANDO LISTA04
        cor = (
    	      (CZ,'Cinza'),
    		  (MR,'Marrom'),
    		  (AM,'Amarelada'),
    		  (TR,'Transparente'),
                 )
        cor =  models.CharField(
             max_length=50,
    		 choices=cor, #DEFINE AS ESCOLHAS
    		 default=TR,#DEFINE O VALOR INICIAL
    		 )
        observacoes = models.CharField(max_length=50)
        foto = models.ImageField()
        # ponto = models.PointField(srid=4326)
# def __str__(self):
#     return self.nome
