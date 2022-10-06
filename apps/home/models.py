from tkinter.tix import CheckList
from django.db import models
from django.contrib.auth.models import User
import uuid

class CMPAChecklist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    location = models.CharField(max_length=30)
    support = models.CharField(max_length=30)
    band_pma = models.IntegerField(default=0, null=True, blank=True)
    band_pmo = models.IntegerField(default=0, null=True, blank=True)
    
    
    def __str__(self):
        return str(self.id)
