import datetime
import logging

from django.contrib.auth.models import User
from django.test import TestCase

logger = logging.getLogger(__name__)


class UserModelTest(TestCase):
    def setUp(self):
        self.u1 = User.objects.create(username="u1", email="u1@gmail.com", is_superuser=True, last_name="u1",
                                      first_name="u1", is_staff=True, is_active=True)
        self.u2 = User.objects.create(username="u2", email="u2@gmail.com", is_superuser=True, last_name="u2",
                                      first_name="u2", is_staff=True, is_active=True)

    def testUser(self):
        self.assertEqual(self.u1.username, "u1")
        self.assertEqual(self.u2.username, "u2")
        logger.debug("Complete User Username Model Test")

        self.assertEqual(self.u1.email, "u1@gmail.com")
        self.assertEqual(self.u2.email, "u2@gmail.com")
        logger.debug("Complete User Email Model Test")

        self.assertEqual(self.u1.is_superuser, True)
        self.assertEqual(self.u2.is_superuser, True)
        logger.debug("Complete User Is SuperUser Model Test")

        self.assertEqual(self.u1.last_name, 'u1')
        self.assertEqual(self.u2.last_name, 'u2')
        logger.debug("Complete User Lastname Model Test")

        self.assertEqual(self.u1.first_name, "u1")
        self.assertEqual(self.u2.first_name, "u2")
        logger.debug("Complete User Firstname Model Test")

        self.assertEqual(self.u1.is_active, True)
        self.assertEqual(self.u2.is_active, True)
        logger.debug("Complete User Is Active Model Test")

    def tearDown(self):
        User.objects.all().delete()
