# Generated by Django 4.2 on 2023-08-28 08:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_record_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='birthday',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='寵物生日'),
        ),
    ]
