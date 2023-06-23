from core.models import BaseModel
from django.db import models

# Create your models here.

class AssetType(BaseModel):
    type_name = models.CharField(max_length=255, default="", blank=False, null=False)
    description = models.TextField(max_length=255)