# Generated by Django 4.0.3 on 2023-07-13 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetdata',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 7, 13, 13, 55, 19, 264626)),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 7, 13, 13, 55, 19, 264626)),
        ),
    ]