import logging

from django.test import TestCase
from django.urls import reverse

logger = logging.getLogger(__name__)


class UserUrlTest(TestCase):
    def testUserLoginURL(self):
        url = reverse("account-login")
        self.assertEqual(url, f"/api/account/login/")
        logger.debug("Complete User Login URL Test")

    def testUserRegisterURL(self):
        url = reverse('account-register')
        self.assertEqual(url, f"/api/account/register/")
        logger.debug("Complete User Register URL Test")

    def testUserLogoutURL(self):
        url = reverse('account-logout')
        self.assertEqual(url, f"/api/account/logout/")
        logger.debug("Complete User Logout URL Test")

    def testUserEditProfileURL(self):
        url = reverse('account-profile-edit')
        self.assertEqual(url, f"/api/account/profile/edit/")
        logger.debug("Complete User Profile Edit URL Test")

    def testUserListURL(self):
        url = reverse('account-list')
        self.assertEqual(url, f"/api/account/user/all/")
        logger.debug("Complete User List URL Test")