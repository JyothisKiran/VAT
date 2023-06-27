# Generated by Django 4.0.3 on 2023-06-27 10:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_type', '0003_alter_assettype_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assettype',
            name='created_at',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 6, 27, 10, 29, 23, 838756)),
        ),
        migrations.AlterField(
            model_name='assettype',
            name='description',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
