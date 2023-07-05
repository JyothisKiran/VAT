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
    financial_year = models.IntegerField()
    asset_owner = models.CharField(max_length=150)
    company_code = models.CharField(max_length=150)
    asset_class = models.IntegerField()
    asset_class_descript = models.CharField(max_length=150)
    asset = models.IntegerField()
    sub_no = models.IntegerField()
    asset_description = models.CharField(max_length=150)
    manufacturer = models.CharField(max_length=150, null=True, blank=True)
    type_name = models.CharField(max_length=150, blank=True, null=True)
    serial_number = models.CharField(max_length=150, blank=True, null=True)
    department = models.IntegerField(blank=True, null=True)
    personnel_number = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150, blank=True, null=True)
    sublocation = models.CharField(max_length=150, blank=True, null=True)
    leasing_company_code = models.IntegerField(blank=True, null=True)
    leasing_company_name = models.CharField(max_length=100, blank=True, null=True)
    capitalization_date = models.CharField(max_length=25, blank=False, null=False)
    plant = models.IntegerField(blank=False, null=False)
    acquisition_value = models.FloatField(blank=False, null=False)
    book_value = models.FloatField(blank=True, null=True)
    high_value_flag = models.CharField(max_length=25, blank=True, null=True)
