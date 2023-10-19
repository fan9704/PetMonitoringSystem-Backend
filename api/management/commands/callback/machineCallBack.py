import json

from api.models import Machine
from api.management.commands.logger.commandLogger import CommandLogger

logger = CommandLogger(__name__).get_logger()


def machine_callback(topic: str, body: str, ch=None, method=None, properties=None):
    logger.debug(f"Topic:{topic} CH:{ch} Method:{method} Properties:{properties}")

    content = json.loads(body)
    machine = Machine.objects.get_or_create(
        name=content["machineId"]
    )
    if content["onlineStatus"]:
        machine.onlineStatus = True
    else:
        machine.onlineStatus = False
    machine.save()
