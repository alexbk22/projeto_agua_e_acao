# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_consulta'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontosColeta',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('pt_id', models.CharField(max_length=80, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4674, null=True, blank=True)),
            ],
            options={
                'db_table': 'pontos_coleta',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='consulta',
            options={'managed': False},
        ),
    ]
