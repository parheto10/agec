# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Commune, Centre, Mairie

admin.site.register(Commune)
admin.site.register(Centre)
admin.site.register(Mairie)

# Register your models here.
