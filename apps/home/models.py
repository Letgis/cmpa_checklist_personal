from django.db import models
import uuid

class CMPAChecklist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user_name = models.CharField(max_length=20, default='', blank=True)
    location = models.CharField(max_length=20, default='', blank=True)
    support = models.CharField(max_length=20, default='', blank=True)
    band_pma = models.CharField(max_length=20, default='', blank=True)
    band_pmo = models.CharField(max_length=20, default='', blank=True)
    project_code = models.CharField(max_length=60, default='', blank=True)
    ippf = models.CharField(max_length=44, default='', blank=True)
    deferral = models.CharField(max_length=44, default='', blank=True)
    customer_name = models.CharField(max_length=100, default='', blank=True)
    contract_tcv = models.CharField(max_length=60, default='', blank=True)
    contract_length = models.CharField(max_length=100, default='', blank=True)
    contract_type = models.CharField(max_length=40, default='', blank=True)
    annual_tcv = models.CharField(max_length=50, default='', blank=True)
    total_invoices = models.CharField(max_length=200, default='', blank=True)
    billing_window = models.CharField(max_length=50, default='', blank=True)
    billing_type = models.CharField(max_length=50, default='', blank=True)
    number_local = models.CharField(max_length=200, default='', blank=True)
    number_ica = models.CharField(max_length=200, default='', blank=True)
    number_sub = models.CharField(max_length=200, default='', blank=True)
    objects = models.Manager()

    class meta:
        db_table = "home_cmpachecklist"
    
    def __str__(self):
        return str(self.id)