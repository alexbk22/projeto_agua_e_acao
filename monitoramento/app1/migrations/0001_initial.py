# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sane',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('nome_do_ponto', models.CharField(default='P1', max_length=50, choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7'), ('P8', 'P8'), ('P9', 'P9'), ('P10', 'P10')])),
                ('data', models.CharField(max_length=50)),
                ('periodo', models.CharField(default='Manha', max_length=50, choices=[('Manha', 'Manha'), ('Tarde', 'Tarde'), ('Noite', 'Noite')])),
                ('observador', models.CharField(max_length=50)),
                ('integrantes', models.CharField(max_length=500)),
                ('od', models.CharField(max_length=50)),
                ('temperatura', models.CharField(max_length=50)),
                ('odor', models.CharField(default='Fraco', max_length=50, choices=[('Forte', 'Forte'), ('Medio', 'Medio'), ('Fraco', 'Fraco'), ('Nenhum', 'Nenhum')])),
                ('cor', models.CharField(default='Transparente', max_length=50, choices=[('Cinza', 'Cinza'), ('Marrom', 'Marrom'), ('Amarelada', 'Amarelada'), ('Transparente', 'Transparente')])),
                ('observacoes', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to=b'')),
            ],
        ),
    ]
