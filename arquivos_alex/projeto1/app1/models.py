from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
# Create your models here.
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
