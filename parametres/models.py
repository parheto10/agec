# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import datetime

class Commune(models.Model):
    region = models.CharField(max_length=250, verbose_name="Region")
    libelle = models.CharField(max_length=250, verbose_name="Commune")

    def save(self, force_insert=False, force_update=False):
        self.region = self.region.upper()
        super(Commune, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "COMMUNES"
        verbose_name = "commune"

    def __unicode__(self):
        return self.libelle

class Mairie(models.Model):
    Commune    = models.ForeignKey(Commune)
    maire      = models.CharField(max_length=500, verbose_name="Nom et Prenoms du Maire")
    telephone1 = models.CharField(max_length=50, verbose_name="Telephone 1")
    telephone2 = models.CharField(max_length=50, verbose_name="Telephone 2", blank=True, null=True)
    adresse    = models.CharField(max_length=100, verbose_name="Adresse Postale", blank=True)
    email      = models.CharField(max_length=100, verbose_name="Adresse Email", blank=True)
    site       = models.CharField(max_length=100, verbose_name="Site Web", blank=True)
    logo       = models.ImageField(upload_to='logos', blank=True, null=True)

    def save(self, force_insert=False, force_update=False):
        self.maire = self.maire.upper()
        super(Mairie, self).save(force_insert, force_update)

    def __unicode__(self):
        return self.Commune.libelle

    class Meta:
        verbose_name_plural = "MAIRIE"
        verbose_name = "mairie"

class Centre(models.Model):
    centre = models.ForeignKey(Commune)
    libelle_centre = models.CharField(max_length=500, verbose_name="Centre de Santé")
    situation = models.CharField(max_length=500, verbose_name="Situation Geographique du Centre")

    def save(self, force_insert=False, force_update=False):
        # self.centre = self.centre.upper()
        self.libelle_centre = self.libelle_centre.upper()
        self.situation = self.situation.upper()
        super(Centre, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "CENTRES DE SANTE"
        verbose_name = "centre de sante"

    def __unicode__(self):
        return self.libelle_centre