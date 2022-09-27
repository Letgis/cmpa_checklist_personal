from tkinter.tix import CheckList
from django.db import models
from django.contrib.auth.models import User
import uuid

class CMPAChecklist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    location = models.CharField(max_length=30)
    supportNeeded = models.CharField(max_length=30)
    bandPMA = models.IntegerField(max_length=1)
    bandPMO = models.IntegerField(max_length=1)
    
    
    def __str__(self):
        return str(self.id)
