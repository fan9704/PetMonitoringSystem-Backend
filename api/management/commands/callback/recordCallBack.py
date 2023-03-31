import json
from api import models


def distanceCallBack(ch, method, properties, body: str):
    print("[Distance]", body.decode(encoding='UTF-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)


def temperatureAndHumidityCallBack(ch, method, properties, body: str):
    print("[Temperature Humidity] Received ", body.decode(encoding='UTF-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)
    machine = models.Machine.objects.get(name=data["machineId"])
    temperatureRecordType = models.RecordType.objects.get(type="Temperature")
    humidityRecordType = models.RecordType.objects.get(type="Humidity")
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


def weightCallBack(ch, method, properties, body: str):
    print("[Weight] Received ", body.decode(encoding='UTF-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)


def waterCallBack(ch, method, properties, body: str):
    print("[Water] Received ", body.decode(encoding='UTF-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    data = json.loads(body)
