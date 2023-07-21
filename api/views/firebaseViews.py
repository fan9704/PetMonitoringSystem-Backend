import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request

from api.serializers import FcmTokenSerializer, UserSerializer
from api.utils import notify
from api import models

logger = logging.getLogger(__name__)


class FcmTokenAPI(APIView):
    @swagger_auto_schema(
        operation_summary='add FCM_Token',
        operation_description='FCM_Token will be use when user need receive message ',
        request_body=FcmTokenSerializer
    )
    def post(self, request: Request):
        fcmToken = models.FcmToken.objects.create(uid_id=request.data.get("uid"), token=request.data.get("token"))
        serializer = FcmTokenSerializer(fcmToken)
        # Send Notify let user now register success

        notify.notify(
            title="Notify Binding",
            body="Success",
            userId=fcmToken.uid.id
        )
        logger.info(f'Send Token Register Notify {fcmToken.uid.id}')
        return Response(serializer.data)
