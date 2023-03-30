import json

from api.models import Machine

def machineCallBack(ch, method, properties, body: str):
    print("[Machine Consumer] Received ", body.decode(encoding='UTF-8'))
    ch.basic_ack(delivery_tag=method.delivery_tag)
    content = json.loads(body)
    machine = Machine.objects.get(name=content["name"])
    if content["status"]:
        machine.onlineStatus = True
    else:
        machine.onlineStatus = False
    machine.save()
