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
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    # machine = models.Machine.objects.get(name=data["machineId"])

    # Check for abnormal temperature
    temperature = float(data["Temperature"])
    if temperature > 27 or temperature < 20:
        raise Exception("溫度異常")

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

    weight = float(data["Weight"])
    if weight < 0:
        raise Exception("進食問題")

    # ch.basic_ack(delivery_tag=method.delivery_tag)


def water_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Water] Received " + str(data["Water"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')

    water = float(data["Water"])
    if water < 0:
        raise Exception("攝取水量問題")
    # ch.basic_ack(delivery_tag=method.delivery_tag)
