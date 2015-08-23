from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Spieler)
admin.site.register(models.EigenEntwicklung)
admin.site.register(models.Anwendungsgebiet)
admin.site.register(models.EETyp)
admin.site.register(models.Effektgruppe)
admin.site.register(models.Effekt)
