# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('gid', models.AutoField(serialize=False, primary_key=True)),
                ('pt_id', models.CharField(max_length=80, null=True, blank=True)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4674, null=True, blank=True)),
            ],
        ),
    ]
