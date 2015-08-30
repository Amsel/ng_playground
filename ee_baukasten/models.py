from django.db import models

# Create your models here.


class Spieler(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class EETyp(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Anwendungsgebiet(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Effektgruppe(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Effekt(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    anwendungsgebiet = models.ForeignKey(Anwendungsgebiet)
    gruppe = models.ManyToManyField(Effektgruppe)
    genehmigt = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class EigenEntwicklung(models.Model):
    name = models.CharField(max_length=127)
    ersteller = models.ForeignKey(Spieler)
    beschreibung = models.TextField(blank=True)
    effekte = models.ManyToManyField(Effekt)
    art = models.ForeignKey(EETyp, default=0)

    def __str__(self):
        return self.name
