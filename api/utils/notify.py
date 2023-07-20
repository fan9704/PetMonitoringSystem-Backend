import logging

import firebase_admin
import os
import requests
import json
from firebase_admin import credentials
from firebase_admin import messaging
from django.contrib.auth.models import User
from api.models import FcmToken

logger = logging.getLogger(__name__)

# from PetMonitoringSystemBackend.settings import FIREBASE_INFO
FIREBASE_INFO = dict({
    "type": os.getenv("FIREBASE_TYPE"),
    "project_id": os.getenv("FIREBASE_PROJECT_ID"),
    "private_key_id": os.getenv("FIREBASE_PRIVATE_KEY_ID"),
    "private_key": os.getenv("FIREBASE_PRIVATE_KEY"),
    "client_email": os.getenv("FIREBASE_CLIENT_EMAIL"),
    "client_id": os.getenv("FIREBASE_CLIENT_ID"),
    "auth_uri": os.getenv("FIREBASE_AUTH_URI"),
    "token_uri": os.getenv("FIREBASE_TOEKN_URI"),
    "auth_provider_x509_cert_url": os.getenv("FIREBASE_AUTH_PROVIDER_X509XCERT_URL"),
    "client_x509_cert_url": os.getenv("FIREBASE_CLIENT_X509_CERT_URL"),
    "universe_domain": os.getenv("FIREBASE_UNIVERSE_DOMAIN"),
})

cred = credentials.Certificate(FIREBASE_INFO)
firebase_admin.initialize_app(cred)


def getUserToken(userId: int = None):
    try:
        if userId is None:
            logger.warning("User ID is None")
        else:
            token = FcmToken.objects.select_related("uid").get(id=userId).token
            return token
    except User.DoesNotExist:
        logger.warning("User.DoesNotExist")


def notify(title: str, body: str, userId: int = None):
    token = getUserToken(userId=userId)
    logger.info(token)
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        data={
            "petname": "Cat1"
        },
        # topic="flutter_notification",
        token=token
    )
    response = messaging.send(message)
    logger.info(f'Successfully sent message User:{userId} Response:{response}')


def httpNotify(title: str, body: str):
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
