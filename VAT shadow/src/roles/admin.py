from django.contrib import admin
from .models import PrivilageMaster, Role

# Register your models here.

admin.site.register(PrivilageMaster)
admin.site.register(Role)