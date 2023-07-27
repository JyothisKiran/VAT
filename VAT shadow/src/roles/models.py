from django.db import models
from core.models import BaseModel
# Create your models here.


class PrivilageMaster(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)


class Role(BaseModel):
    ROLE_CHOICES = (( 'Admin', 'Admin'), ( 'Auditor', 'Auditor'))

    role_name = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100, choices=ROLE_CHOICES)
    description = models.CharField(max_length=120, blank=True, null=True)
