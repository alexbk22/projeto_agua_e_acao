# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20180706_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultaSane',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_do_ponto', models.CharField(max_length=50)),
                ('data', models.CharField(max_length=50)),
                ('periodo', models.CharField(max_length=50)),
                ('observador', models.CharField(max_length=50)),
                ('integrantes', models.CharField(max_length=500)),
                ('od', models.CharField(max_length=50)),
                ('temperatura', models.CharField(max_length=50)),
                ('odor', models.CharField(max_length=50)),
                ('cor', models.CharField(max_length=50)),
                ('observacoes', models.CharField(max_length=50)),
                ('foto', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='consulta',
            options={},
        ),
    ]
