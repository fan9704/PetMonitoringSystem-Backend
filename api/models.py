import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class PetType(models.Model):
    typename = models.CharField(max_length=25, null=True, blank=True, verbose_name="寵物種類")
    description = models.TextField(null=True, blank=True, verbose_name="寵物種類描述")

    def __str__(self):
        return f'寵物種類{self.typename}'


class Pet(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=256, verbose_name="寵物名稱")
    keeper = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="寵物照顧人")
    type = models.ForeignKey(to=PetType, on_delete=models.CASCADE, verbose_name="寵物種類")
    birthday = models.DateField(verbose_name="寵物生日", blank=True, null=True, default=datetime.date.today)
    content = models.TextField(verbose_name="寵物敘述")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="寵物重量")  # 新增寵物重量欄位
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='unknown', verbose_name="性別")  # 新增性別欄位
    is_neutered = models.BooleanField(default=False, verbose_name="是否結紮")   # 新增結紮欄位
    activity_level = models.CharField(max_length=10,
                                      choices=[('low', 'Low'), ('moderate', 'Moderate'), ('high', 'High')])
    der = models.DecimalField(max_digits=6, decimal_places=2, default=0, verbose_name="每日能量需求")    # der欄位
    image = models.ImageField(upload_to=upload_to, blank=True, null=True)


    # External Columns
    # chip_id = models.CharField(max_length=256,verbose_name="晶片編號")
    # coat_color = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}  照顧人:{self.keeper.username}:   寵物種類{self.type.typename}'



class Machine(models.Model):
    name = models.CharField(max_length=255, verbose_name="機器名稱")
    onlineStatus = models.BooleanField(default=False, verbose_name="上線狀態")
    pet = models.ForeignKey(to=Pet, on_delete=models.CASCADE, null=True, default=None, verbose_name="綁定寵物")

    def __str__(self):
        return f'機器名稱{self.name} 狀態:{self.onlineStatus} 綁定寵物:{self.pet.name}'


class RecordType(models.Model):
    type = models.CharField(max_length=255, verbose_name="紀錄種類")

    def __str__(self):
        return f'類別:{self.type}'


class Record(models.Model):
    pet = models.ForeignKey(to=Pet, on_delete=models.CASCADE, verbose_name="寵物ID")
    type = models.ForeignKey(to=RecordType, on_delete=models.CASCADE, verbose_name="記錄種類")
    data = models.FloatField(null=True, blank=True, verbose_name="數據值")
    time = models.DateTimeField(blank=True, default=timezone.now, verbose_name="紀錄時間")

    def __str__(self):
        return f'數據{self.data}'


class FcmToken(models.Model):
    uid = models.ForeignKey(User, db_column="uid", on_delete=models.CASCADE, verbose_name='使用者ID')
    token = models.CharField(max_length=255, null=True, blank=True, verbose_name="Fcm_Token")
