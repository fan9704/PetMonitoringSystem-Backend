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
    logger.info("Firebase Enabled")
    cred = credentials.Certificate(settings.FIREBASE_CONFIG)
    firebase_admin.initialize_app(credential=cred)


def get_user_token(user_id: int = None):
    try:
        if user_id is None:
            logger.warning("User ID is None")
            return None
        else:
            fcm = FcmToken.objects.select_related("uid").get(id=user_id)
            return fcm.token
    except FcmToken.DoesNotExist:
        logger.warning("User/Token DoesNotExist")
        return None


def notify(title: str, body: str, user_id: int = None):
    token = get_user_token(user_id=user_id)
    if token :
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
    else:
        logger.info(f'Token is invalid {token} User:{user_id}')