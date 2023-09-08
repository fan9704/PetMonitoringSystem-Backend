import json
import logging
from api import models
from api.management.commands.logger.commandLogger import CommandLogger

# logger = logging.getLogger("Record Listener")
logger = CommandLogger("Record Listener").getLogger()


def distanceCallBack(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Distance] Received " + str(data["Distance"]))
    # ch.basic_ack(delivery_tag=method.delivery_tag)


def temperatureAndHumidityCallBack(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Temperature] Received " + str(data["Temperature"]))
    logger.info("[Humidity] Received " + str(data["Humidity"]))
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
    temperatureRecordType = models.RecordType.objects.get(type="temperature")
    humidityRecordType = models.RecordType.objects.get(type="humidity")
    temperature = models.Record.objects.create(
        pet=machine.pet,
        type=temperatureRecordType,
        data=data["Temperature"],
    )
    humidity = models.Record.objects.create(
        pet=machine.pet,
        type=humidityRecordType,
        data=data["Humidity"],
    )
    temperature.save()
    humidity.save()


def weightCallBack(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Weight] Received " + str(data["Weight"]))

    weight = float(data["Weight"])
    if weight < 0:
        raise Exception("進食問題")

    # ch.basic_ack(delivery_tag=method.delivery_tag)


def waterCallBack(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Water] Received " + str(data["Water"]))

    water = float(data["Water"])
    if water < 0:
        raise Exception("攝取水量問題")
    # ch.basic_ack(delivery_tag=method.delivery_tag)
