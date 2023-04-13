import json

from api.models import Machine


def machineCallBack(topic: str, body: str, ch=None, method=None, properties=None):
    print("[Machine] Received ", body)
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    content = json.loads(body)
    try:
        machine = Machine.objects.get(
            name=content["machineId"]
        )
    except Machine.DoesNotExist:
        machine = Machine.objects.create(
            name=content["machineId"]
        )
    if content["onlineStatus"]:
        machine.onlineStatus = True
    else:
        machine.onlineStatus = False
    machine.save()
