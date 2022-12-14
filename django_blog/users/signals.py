from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''Создание профиля после регистрации'''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''Сохраняет профиль'''
    instance.profile.save()



#----> apps.py    
