import json
from api import models
from api.management.commands.logger.commandLogger import CommandLogger

logger = CommandLogger(__name__).get_logger()


def distance_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Distance] Received " + str(data["Distance"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')


def temperature_humidity_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Temperature] Received " + str(data["Temperature"]))
    logger.info("[Humidity] Received " + str(data["Humidity"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')
    try:
        machine = models.Machine.objects.get(name=topic.split("/")[1])
    except models.Machine.DoesNotExist:
        machine = models.Machine.objects.create(
            name=topic.split("/")[1]
        )
    temperature_record_type = models.RecordType.objects.get(type="temperature")
    humidity_record_type = models.RecordType.objects.get(type="humidity")
    temperature = models.Record.objects.create(
        pet=machine.pet,
        type=temperature_record_type,
        data=data["Temperature"],
    )
    humidity = models.Record.objects.create(
        pet=machine.pet,
        type=humidity_record_type,
        data=data["Humidity"],
    )
    temperature.save()
    humidity.save()


def weight_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Weight] Received " + str(data["Weight"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')


def water_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Water] Received " + str(data["Water"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')
