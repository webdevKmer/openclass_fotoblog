from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

    ROLE_CHOICES = ((CREATOR, 'Createur'), (SUBSCRIBER, 'Abonne'),)

    profile_photo = models.ImageField(verbose_name="Photo de profil")
    role = models.CharField(verbose_name='Role', max_length=20, choices=ROLE_CHOICES)