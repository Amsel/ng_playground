from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.PlayerCreation)
admin.site.register(models.EffectCategory)
admin.site.register(models.Effect)
admin.site.register(models.Character)
admin.site.register(models.PlayerCreationCategory)
admin.site.register(models.UseCase)

