from django.db import models
from django.utils import timezone

from core.models import BaseModel

# Create your models here.


class AssetData(BaseModel):
    filename = models.CharField(max_length=50, null=False, blank=False)
    start_date = models.DateTimeField(default=timezone.now, blank=False, null=False)
    end_date = models.DateTimeField(default=timezone.now, blank=False, null=False)
    file = models.FileField(blank=False, null=False)


class DataModel(BaseModel):
    financial_year = models.CharField(max_length=150,)
    asset_owner = models.CharField(max_length=150)
    company_code = models.CharField(max_length=150)
    asset_class = models.CharField(max_length=150,)
    asset_class_descript = models.CharField(max_length=150)
    asset = models.CharField(max_length=150,)
    sub_no = models.CharField(max_length=150,)
    asset_description = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    type_name = models.CharField(max_length=150, blank=True, null=True)
    serial_number = models.CharField(max_length=150, blank=True, null=True)
    department = models.CharField(max_length=150, blank=True, null=True)
    personnel_number = models.CharField(max_length=150, blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    sublocation = models.CharField(max_length=150, blank=True, null=True)
    leasing_company_code = models.CharField(max_length=150, blank=True, null=True)
    leasing_company_name = models.CharField(max_length=100, blank=True, null=True)
    capitalization_date = models.CharField(max_length=25, blank=False, null=False)
    plant = models.CharField(max_length=150, blank=False, null=False)
    acquisition_value = models.CharField(max_length=150, blank=False, null=False)
    book_value = models.CharField(max_length=150, blank=True, null=True)
    high_value_flag = models.CharField(max_length=25, blank=True, null=True)
