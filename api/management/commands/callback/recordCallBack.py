import json
from api import models
from api.management.commands.logger.commandLogger import CommandLogger
from api.utils.notify import notify

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

    # Check for abnormal temperature
    temperature = float(data["Temperature"])
    humidity = float(data["Humidity"])
    if temperature > 27 or temperature < 20:
        notify_content = f'''
        [寵物環境溫度] {temperature}
        [寵物環境濕度] {humidity}
        '''
        notify("溫度異常", notify_content, 1)
    machine, _ = models.Machine.objects.get_or_create(name=topic.split("/")[1])
    if machine.pet is None:
        machine.pet = models.Pet.objects.get(pk=1)
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
    machine, _ = models.Machine.objects.get_or_create(name=topic.split("/")[1])
    weight_record_type = models.RecordType.objects.get(type="weight")

    weight = float(data["Weight"])
    if weight < 0:
        notify_content = f'''
        [寵物進食量] {weight}
        '''
        notify("進食過少", notify_content, 1)

    weight = models.Record.objects.create(
        pet=machine.pet,
        type=weight_record_type,
        data=data["Weight"],
    )
    weight.save()


def water_callback(topic: str, body: str, ch=None, method=None, properties=None):
    data = json.loads(body)
    logger.info("[Water] Received " + str(data["Water"]))
    logger.debug(f'Topic:{topic} ch:{ch} properties:{properties} method:{method}')
    machine, _ = models.Machine.objects.get_or_create(name=topic.split("/")[1])
    water_record_type = models.RecordType.objects.get(type="water")

    water = float(data["Water"])
    if water < 0:
        notify_content = f'''
        [寵物喝水量] {water}
        '''
        notify("喝水過少", notify_content, 1)

    water = models.Record.objects.create(
        pet=machine.pet,
        type=water_record_type,
        data=data["Water"],
    )
    water.save()
