# Generated by Django 4.0.3 on 2023-07-13 13:55

from django.db import migrations
from ..config import add_privilage


def add_roles(apps, schema):
    add_privilage()


class Migration(migrations.Migration):

    dependencies = [
        ( 'roles', '0001_initial'),
    ]

    operations = [migrations.RunPython(add_roles)]
