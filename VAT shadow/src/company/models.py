from django.db import models
from core.models import BaseModel

# Create your models here.


class Company(BaseModel):
    company_name = models.CharField(max_length=100)
    company_code = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
