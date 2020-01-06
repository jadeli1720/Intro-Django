from django.db import models
from uuid import uuid4

class User(models.Model):
    id = models.UUIDField(primary_key = True, default =uuid4, editable=False )
    name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=200, unique=True)