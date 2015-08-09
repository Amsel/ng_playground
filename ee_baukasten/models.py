from django.db import models

# Create your models here.


class Spieler(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class EigenEntwicklung(models.Model):
    name = models.CharField(max_length=127)
    ersteller = models.ForeignKey(Spieler)

    def __str__(self):
        return self.name


class Anwendungsgebiet(models.Model):
    name = models.CharField(max_length=127)

    def __str__(self):
        return self.name


class Effekt(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField()
    entwicklungen = models.ManyToManyField(EigenEntwicklung)
    anwendungsgebiet = models.ForeignKey(Anwendungsgebiet)

    def __str__(self):
        return self.name



