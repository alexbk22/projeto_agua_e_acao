# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class App1Capitaisponto(models.Model):
    gid = models.AutoField(primary_key=True)
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    cd_geocmu = models.CharField(max_length=7, blank=True, null=True)
    geom = models.PointField(srid=4674, blank=True, null=True)
    regiao = models.CharField(max_length=15, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'app1_capitaisponto'


class App1Consulta(models.Model):
    gid = models.AutoField(primary_key=True)
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    cd_geocmu = models.CharField(max_length=7, blank=True, null=True)
    geom = models.PointField(srid=4674, blank=True, null=True)
    regiao = models.CharField(max_length=15, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'app1_consulta'


class App1Estados(models.Model):
    gid = models.AutoField(primary_key=True)
    nm_estado = models.CharField(max_length=50, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)
    cd_geocuf = models.CharField(max_length=2, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'app1_estados'


class CapitaisPonto(models.Model):
    gid = models.AutoField(primary_key=True)
    nm_municip = models.CharField(max_length=60, blank=True, null=True)
    cd_geocmu = models.CharField(max_length=7, blank=True, null=True)
    geom = models.PointField(srid=4674, blank=True, null=True)
    regiao = models.CharField(max_length=15, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'capitais_ponto'


class Estados(models.Model):
    gid = models.AutoField(primary_key=True)
    nm_estado = models.CharField(max_length=50, blank=True, null=True)
    nm_regiao = models.CharField(max_length=20, blank=True, null=True)
    cd_geocuf = models.CharField(max_length=2, blank=True, null=True)
    geom = models.MultiPolygonField(srid=4674, blank=True, null=True)
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'estados'


class Layer(models.Model):
    topology = models.ForeignKey('Topology')
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=-1)
    table_name = models.CharField(max_length=-1)
    feature_column = models.CharField(max_length=-1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'
        unique_together = (('topology_id', 'layer_id'), ('schema_name', 'table_name', 'feature_column'),)


class Topology(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'
