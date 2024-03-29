# Generated by Django 4.2 on 2023-09-08 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_pet_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='activity_level',
            field=models.CharField(choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')], default='Low', max_length=10),
        ),
        migrations.AddField(
            model_name='pet',
            name='der',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='每日能量需求'),
        ),
        migrations.AddField(
            model_name='pet',
            name='gender',
            field=models.BooleanField(default=False, verbose_name='性別'),
        ),
        migrations.AddField(
            model_name='pet',
            name='is_neutered',
            field=models.BooleanField(default=False, verbose_name='是否結紮'),
        ),
        migrations.AddField(
            model_name='pet',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, verbose_name='寵物重量'),
        ),
        migrations.AlterField(
            model_name='fcmtoken',
            name='token',
            field=models.CharField(default='', max_length=255, verbose_name='Fcm_Token'),
        ),
        migrations.AlterField(
            model_name='pettype',
            name='description',
            field=models.TextField(default='', verbose_name='寵物種類描述'),
        ),
        migrations.AlterField(
            model_name='pettype',
            name='typename',
            field=models.CharField(default='', max_length=25, verbose_name='寵物種類'),
        ),
    ]
