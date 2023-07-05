from django.db import models

from core.models import BaseModel

# Create your models here.


class AssetType(BaseModel):
    type_name = models.CharField(max_length=255, default="", blank=False, null=False)
    description = models.CharField(max_length=255, blank=True, null=True)
