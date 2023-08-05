import logging

import firebase_admin
import os
import requests
import json
from firebase_admin import credentials, messaging
from django.contrib.auth.models import User
from django.conf import settings
from api.models import FcmToken

logger = logging.getLogger(__name__)

if settings.FIREBASE_ENABLE:
    cred = credentials.Certificate(settings.FIREBASE_CONFIG)
    firebase_admin.initialize_app(credential=cred)


def get_user_token(user_id: int = None):
    try:
        if user_id is None:
            logger.warning("User ID is None")
        else:
            token = FcmToken.objects.select_related("uid").get(id=user_id).token
            return token
    except User.DoesNotExist:
        logger.warning("User.DoesNotExist")


def notify(title: str, body: str, user_id: int = None):
    token = get_user_token(user_id=user_id)
    logger.info(token)
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data={
            "petname": "Cat1"
        },
        token=token
    )
    response = messaging.send(message)
    logger.info(f'Successfully sent message User:{user_id} Response:{response}')


def http_notify(title: str, body: str):
    FCM_API_KEY = "ya29.a0AbVbY6MSnYsqSopTQnm-TqfK0ixgIDOo1SdVxMcPWeKylVOET28z5DpWAi0zijymxs-OBzu5xGrD3p0qY1Ks1lN2P_Sxo9yaWG3aDNIlKsU9qc35ZxxvDSBR6vdlNApEBoNHo51Kf59jsQl2Nk5Q82-N3fXSaCgYKAfwSARMSFQFWKvPlpuxoXdVqHg-r3pEBsp-N3A0163"
    FCM_TOKEN = os.getenv("FCM_DEVICE_TOKEN", None)

    message = {
        "message": {
            "token": FCM_TOKEN,
            "data": {
                "body": body,
                "title": title,
                "key_1": "Value for key_1",
                "key_2": "Value for key_2"
            }
        }
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {FCM_API_KEY}'
    }
    response = requests.post('https://fcm.googleapis.com/v1/projects/petmonitoringsystem-729da/messages:send',
                             data=json.dumps(message), headers=headers)
    print(response.text)


if '__main__' == __name__:
    notify("TEST", "Python SDK", 1)
