from django.db import models
from django.utils import timezone

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)

    class Meta:
        abstract = True