import firebase_admin
import os
import requests
import json
from firebase_admin import credentials
from firebase_admin import messaging
from PetMonitoringSystemBackend.settings import FIREBASE_INFO

cred = credentials.Certificate(FIREBASE_INFO)
firebase_admin.initialize_app(cred)


def notify(title: str, body: str):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=os.getenv("FCM_DEVICE_TOKEN")
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)


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
