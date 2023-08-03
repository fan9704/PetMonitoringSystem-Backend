# Command python manage.py seed
import logging
import os

from django_seed import Seed
from django.contrib.auth.models import User
from api.models import RecordType
from api.models import PetType
from dotenv import load_dotenv


load_dotenv()
logger = logging.getLogger(__name__)


def generate_pet_type_seed_data():
    pet_type_dict = {
        "Cat": "This is a pet cat.",
        "Dog": "This is a pet dog.",
        "Mouse": "This is a pet mouse.",
        "Other": "This is an other pet type."
    }

    seeder = Seed.seeder("PetType")
    for pet_name, pet_description in pet_type_dict.items():
        seeder.add_entity(PetType, 1, {
            'typename': pet_name,
            'description': pet_description,
        })
    inserted_pks = seeder.execute()
    logger.info(inserted_pks)
    logger.info("Created Pet Type Seed Data")


def generate_admin_user_seed_data():
    seeder = Seed.seeder("Admin")
    seeder.add_entity(User, 1, {
        "username": "admin",
        "password": os.getenv("PGADMIN_DEFAULT_PASSWORD"),
        "email": "admin@gmail.com",
        "is_superuser": True,
        "is_staff": True,
        "first_name": "admin",
        "last_name": "admin",
    })
    inserted_pks = seeder.execute()
    logger.info(inserted_pks)
    logger.info("Created Admin User Seed Data")


def generate_record_type_seed_data():
    seeder = Seed.seeder("RecordType")
    record_type_list = ["weight", "water", "humidity", "temperature", "food"]
    for i in record_type_list:
        seeder.add_entity(RecordType, 1, {
            "type": i
        })
    inserted_pks = seeder.execute()
    logger.info(inserted_pks)
    logger.info("Created Record Type Seed Data")


if __name__ == '__main__':
    logger.info("Start Init Seed Data")
    generate_record_type_seed_data()
    generate_admin_user_seed_data()
    generate_pet_type_seed_data()
    logger.info("Complete Created All Seed Data")
