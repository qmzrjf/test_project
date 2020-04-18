from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from profile_app import model_choices as mch


class Customer(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)
    biography = models.TextField()
    date_of_birth = models.DateField(default=timezone.now, blank=True)


class Logger(models.Model):
    user = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    action = models.CharField(choices=mch.ACTION_CHOICES, max_length=13)


class LoggerEditProfile(models.Model):
    user = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=100, null=True, blank=True)
