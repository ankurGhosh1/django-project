from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile', null=True)

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    
class Watchlist(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    symbol = models.CharField(max_length=10)

    def __str__(self):
        return self.symbol