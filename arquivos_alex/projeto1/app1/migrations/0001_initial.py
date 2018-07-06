# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App1Capitaisponto',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('nm_municip', models.CharField(max_length=60, null=True, blank=True)),
                ('cd_geocmu', models.CharField(max_length=7, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4674, null=True, blank=True)),
                ('regiao', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'app1_capitaisponto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Consulta',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('nm_municip', models.CharField(max_length=60, null=True, blank=True)),
                ('cd_geocmu', models.CharField(max_length=7, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4674, null=True, blank=True)),
                ('regiao', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'app1_consulta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='App1Estados',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('nm_estado', models.CharField(max_length=50, null=True, blank=True)),
                ('nm_regiao', models.CharField(max_length=20, null=True, blank=True)),
                ('cd_geocuf', models.CharField(max_length=2, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674, null=True, blank=True)),
            ],
            options={
                'db_table': 'app1_estados',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CapitaisPonto',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('nm_municip', models.CharField(max_length=60, null=True, blank=True)),
                ('cd_geocmu', models.CharField(max_length=7, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4674, null=True, blank=True)),
                ('regiao', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'capitais_ponto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Estados',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('nm_estado', models.CharField(max_length=50, null=True, blank=True)),
                ('nm_regiao', models.CharField(max_length=20, null=True, blank=True)),
                ('cd_geocuf', models.CharField(max_length=2, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4674, null=True, blank=True)),
            ],
            options={
                'db_table': 'estados',
                'managed': False,
            },
        ),
    ]
