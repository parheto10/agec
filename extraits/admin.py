# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Jugement, Mention, Naissance

class MentionInline(admin.TabularInline):
    model = Mention
    extra = 1
    #fields = ['categorie', 'numero', 'date_mariage', 'heure_mariage', 'lieu_mariage']
    verbose_name_plural = "MENTIONS EVENTUELLES"
    verbose_name = "Mention"
# class BookAdmin(admin.ModelAdmin):
#     fieldsets = [ (None, {'fields': ['title'}) ]
#     inlines = [ TransactionInline, ]

class ExtraitsAdmin(admin.ModelAdmin):
    list_display = ['numero_registre', 'nom', 'prenoms', 'date_naiss', 'pere', 'mere']
    list_display_links = ['numero_registre',]
    search_fields = ['numero_registre', ]
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": (('annee', 'numero_registre'), ('categorie'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": (('sexe', 'hopital') ,('nom', 'prenoms'), ('date_naiss', 'heure_naiss'), ('jugement', 'num_jugement'), )}),
        ('PARENTS', {"fields": (('mere', 'profession_mere'), ('pere', 'profession_pere'), )}),
        #('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )
    inlines = [
        MentionInline,
    ]



admin.site.register(Jugement)
#admin.site.register(Mention)
admin.site.register(Naissance, ExtraitsAdmin)

# Register your models here.
