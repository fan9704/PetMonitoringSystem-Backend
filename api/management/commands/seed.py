import logging
import os

import logstash
from django.core.management.base import BaseCommand

from api import models

logger = logging.getLogger("Django Database Seed")

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'
""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clearRecordTypeData():
    """Deletes all the table data"""
    logger.info("Delete Record Type instances")
    models.RecordType.objects.all().delete()


def createRecordType():
    """Creates an address object combining different elements from the list"""
    logger.info("Creating Record Type DataSeed")
    recordTypeDict = dict()
    recordTypeDict[1] = "weight"
    recordTypeDict[2] = "water"
    recordTypeDict[3] = "humidity"
    recordTypeDict[4] = "temperature"
    recordTypeDict[5] = "food"

    for index,name in recordTypeDict.items():
        recordType = models.RecordType.objects.create(
            id = index,
            type = name
        )
        recordType.save()

        logger.info("{} Record Type Created.".format(recordType))


def run_seed(self, mode=None):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    clearRecordTypeData()
    if mode == MODE_CLEAR:
        return
    createRecordType()
