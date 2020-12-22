from django.db import models

# Create your models here.

class Gouvernorat(models.Model):
    gouvernorat_id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=25)

class Statistique(models.Model):
    statistiqu_id = models.AutoField(primary_key=True)
    cas_positif = models.CharField(max_length=10)
    deces = models.CharField(max_length=10)
    guerison = models.CharField(max_length=10)
    cas_actif = models.CharField(max_length=10)
    datest = models.CharField(max_length=10)
    gouvernorat_FK = models.ForeignKey(Gouvernorat,on_delete=models.CASCADE)
