# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as User
from django.db.models.signals import post_save
# Create your models here.

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(verbose_name='Phone number', max_length=100)
    address = models.CharField(verbose_name='Address', max_length=300)

class ReporterProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    gender = models.CharField(max_length = 10)

class AgentProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)