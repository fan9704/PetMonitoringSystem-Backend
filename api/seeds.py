# Command python manage.py seed

from django_seed import Seed
from django.contrib.auth.models import User
from api.models import RecordType
from api.models import PetType


def generatePetTypeSeedData():
    petTypeDict = {
        "Cat": "This is a pet cat.",
        "Dog": "This is a pet dog.",
        "Mouse": "This is a pet mouse.",
        "Other": "This is an other pet type."
    }

    seeder = Seed.seeder("PetType")
    for petName, petDescription in petTypeDict.items():
        seeder.add_entity(PetType, 1, {
            'typename': petName,
            'description': petDescription,
        })
    inserted_pks = seeder.execute()


def generateAdminUserSeedData():
    seeder = Seed.seeder("Admin")
    seeder.add_entity(User, 1, {
        "username": "admin",
        "password": "admin",
        "email": "admin@gmail.com",
        "is_superuser": True,
        "is_staff": True,
        "first_name": "admin",
        "last_name": "admin",
    })
    inserted_pks = seeder.execute()


def generateRecordTypeSeedData():
    seeder = Seed.seeder("RecordType")
    recordTypeList = ["weight", "water", "humidity", "temperature", "food"]
    for i in recordTypeList:
        seeder.add_entity(RecordType, 1, {
            "type": i
        })
    inserted_pks = seeder.execute()


if __name__ == '__main__':
    generatePetTypeSeedData()
    generateAdminUserSeedData()
    generateRecordTypeSeedData()
