# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
import datetime
from parametres.models import Commune, Centre, Mairie

Categorie = (
    ('ACTE DE NAISSANCES',(
        ("normal", "NORMAL"),
        ("copie", "COPIE INTEGRALE / JUGEMENT SUPPLETIF"),
        )
     ),
    ('MENTIONS',(
        ('mariage', 'ACTE DE MARIAGE'),
        ('deces', 'ACTE DE DECES'),
        )
    )
)

def number():
    no = Naissance.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Jugement(models.Model):

    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    # Infos Gles
    numero_registre = models.CharField(max_length=150, verbose_name='Numero du Registre')
    annee = models.IntegerField(verbose_name='Annee de Naissance', choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year)
    categorie = models.CharField(max_length=150, verbose_name='Nature Document', choices=Categorie, default="copie")

    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='Precise le sexe', choices=Sexe)
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    date_naiss = models.DateField(verbose_name='Date de Naissance')
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    hopital = models.ForeignKey(Centre)
    commune = models.ForeignKey(Commune)
    officie = models.CharField(max_length=500, verbose_name="Nom et Prenoms Officie")

    # parents
    pere = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere', blank=True)
    date_naiss_pere = models.DateField(verbose_name='Date de Naissance du Pere', blank=True)
    lieu_naiss_pere = models.DateField(verbose_name='Lieu de Naissance du Pere', blank=True)
    profession_pere = models.CharField(max_length=250, verbose_name='Profession du Pere', blank=True)
    domicile_pere = models.CharField(max_length=250, verbose_name='Domicile du pere')

    mere = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere')
    date_naiss_mere = models.DateField(verbose_name='Date de Naissance de la mere')
    lieu_naiss_mere = models.DateField(verbose_name='Lieu de Naissance de la mere')
    profession_mere = models.CharField(max_length=250, verbose_name='Profession de la mere', blank=True)
    domicile_meree = models.CharField(max_length=250, verbose_name='Domicile de la mere')
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = "JUGEMENTS SUPPLETIFS"
        verbose_name = "Jugement Suppletif"

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        self.hopital = self.hopital.upper()
        self.officie = self.officie.upper()

        self.pere = self.pere.upper()
        self.lieu_naiss_pere = self.lieu_naiss_pere.upper()
        self.domicile_pere = self.domicile_pere.upper()

        self.mere = self.mere.upper()
        self.lieu_naiss_mere = self.lieu_naiss_mere.upper()
        self.domicile_mere = self.domicile_mere.upper()
        super(Jugement, self).save(force_insert, force_update)




class Naissance(models.Model):

    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    Jugement_Choice = (
        ('oui', 'OUI'),
        ('non', 'NON')
    )

    # Infos Gles
    numero_registre = models.CharField(max_length=150, verbose_name='Numero du Registre')
    annee = models.IntegerField(verbose_name='Annee de Naissance', choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year)
    categorie = models.CharField(max_length=150, verbose_name='Nature Document', choices=Categorie, default="normal")
    #centre = models.ForeignKey(Centre)

    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='Precise le sexe', choices=Sexe)
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    date_naiss = models.DateField(verbose_name='Date de Naissance')
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    hopital = models.ForeignKey(Centre)
    jugement = models.CharField(max_length=5, verbose_name="TRANSCRIPTION DE JUGEMENT SUPPLETIF ?", choices=Jugement_Choice, default="non")
    num_jugement = models.CharField(max_length=255, verbose_name="PRECISER LE NUMERO DU JUGEMENT SUPPLETIF", blank=True)

    # parents
    pere = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere', blank=True)
    profession_pere = models.CharField(max_length=250, verbose_name='Profession du Pere', blank=True)
    mere = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere')
    profession_mere = models.CharField(max_length=250, verbose_name='Profession de la Mere')
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    def clean(self):
        if self.jugement == "non" and self.num_jugement != "": raise ValidationError(
            "ERREUR CORRIGER SVP !!")
        else:
            if self.jugement =="oui" and self.num_jugement =="": raise ValidationError(
                "VEUILLEZ PRECISER LE NUMERO DU JUGEMENT SUPPLETIF SVP"
            )

    class Meta:
        verbose_name_plural = "ACTES DE NAISSANCE"
        verbose_name = "Acte de naissance"

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        #self.hopital = self.hopital.upper()
        self.pere = self.pere.upper()
        self.mere = self.mere.upper()
        super(Naissance, self).save(force_insert, force_update)


class Mention(models.Model):
    Regime = (
        ('simple', 'SIMPLE'),
        ('communaute', 'COMUAUTE DE BIEN'),
    )

    #info Gles
    requerant = models.ForeignKey(Naissance)
    categorie = models.IntegerField(verbose_name='Type de Document', choices=Categorie)
    numero = models.CharField(max_length=5, unique=True, verbose_name="Numero Mariage", blank=True)
    date_mariage = models.DateField(verbose_name="Date du Mariage", blank=True)
    heure_mariage = models.DateField(verbose_name="Heure du Mariage", blank=True)
    lieu_mariage = models.CharField(max_length=500, verbose_name="Lieu de Celebartion du Mariage", blank=True)

    #Avec(Conjoint/conjointe)
    conjoint = models.CharField(max_length=150, verbose_name="Nom et Prenoms du CONJOINT(E)", blank=True)

    #divorce
    date_divorce = models.DateField(max_length=250, verbose_name="Date du Divorce", blank=True)
    details_divorce = models.CharField(max_length=250, verbose_name="Details Divorce", blank=True)

    # divorce
    date_deces = models.DateField(max_length=250, verbose_name="Date du Deces")
    lieu_deces = models.CharField(max_length=250, verbose_name="Lieu du Deces")
    cause_deces = models.CharField(max_length=250, verbose_name="Cause du Deces")

    # class Meta:
    #     verbose_name_plural = "MENTIONS EVENTUELLES"
    #     verbose_name = "Mention"

# Create your models here.
