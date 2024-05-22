from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    tickets = models.ManyToManyField('tickets.Ticket', blank=True, related_name='users')
