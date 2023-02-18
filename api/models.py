from django.contrib.auth.models import User
from django.db import models


class PetType(models.Model):
    typename = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'寵物種類{self.typename}'


class Pet(models.Model):
    name = models.CharField(max_length=256)
    keeper = models.ForeignKey(to=User, on_delete=models.CASCADE)
    type = models.ForeignKey(to=PetType, on_delete=models.CASCADE)
    birthday = models.DateField()
    content = models.TextField()

    def __str__(self):
        return f'{self.name}  照顧人 {self.keeper.username}:   寵物種類{self.type.typename}'


class Machine(models.Model):
    name = models.CharField(max_length=255)


class RecordType(models.Model):
    type = models.CharField(max_length=255)


class Record(models.Model):
    pet = models.ForeignKey(to=Pet, on_delete=models.CASCADE)
    type = models.ForeignKey(to=RecordType, on_delete=models.CASCADE)
    data = models.FloatField(null=True, blank=True)
    machine = models.ForeignKey(to=Machine, on_delete=models.CASCADE)
