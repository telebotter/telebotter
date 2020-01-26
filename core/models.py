from django.db import models
import datetime as dt
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Bot(models.Model):
    name = models.CharField(max_length=60, null=True, blank=True)
    username = models.CharField(max_length=60, null=True, blank=True)
    token = models.CharField(max_length=128, null=True, blank=True)
    short = models.TextField(null=True, blank=True)
    long = models.TextField(null=True, blank=True)
    public = models.BooleanField(default=True)
    promote = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    avatar_thumbnail = ImageSpecField(source='avatar',
                                      processors=[ResizeToFill(140, 140)],
                                      format='png')
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.name)


class TelebotUser(models.Model):
    user_id = models.BigIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    username = models.CharField(max_length=60, null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name)
