import json

from api.models import Machine
from api.management.commands.logger.commandLogger import CommandLogger

logger = CommandLogger(__name__).get_logger()


def machine_callback(topic: str, body: str, ch=None, method=None, properties=None):
    logger.debug(f"Topic:{topic} CH:{ch} Method:{method} Properties:{properties}")

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
