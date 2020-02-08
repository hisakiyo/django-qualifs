from django.db import models
from django.contrib.auth.models import User

# Utilisateur lié à Django User
class InfoUser(models.Model):
    id = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE, primary_key=True)
    prefere = models.IntegerField()
    ban = models.BooleanField()

# Vaisseau
class Vaisseau(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=250)
    empruter = models.BooleanField()
    etat = models.IntegerField()

# Tableau des emprunts
class Emprunt(models.Model):
    id = models.OneToOneField(User, to_field='id', on_delete=models.CASCADE, primary_key=True)
    id_vaisseau =  models.ForeignKey(Vaisseau, to_field='id', on_delete=models.CASCADE, primary_key=False)
    date_emprunt = models.DateTimeField()
    date_retour = models.DateTimeField()