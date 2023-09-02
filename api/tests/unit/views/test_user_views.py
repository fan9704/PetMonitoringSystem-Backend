import logging
import secrets
from types import SimpleNamespace

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory

from api.views.userViews import Register, LogoutAPI, EditProfileAPI, UserAPIView, OAuthUserRegisterAPI, \
    OAuthUserLoginAPI
from django.contrib.sessions.middleware import SessionMiddleware

logger = logging.getLogger(__name__)


class UserAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def tearDown(self) -> None:
        User.objects.all().delete()

    def test_register_new_user(self):
        data = {
            "username": "test_003",
            "password": str(secrets.randbits(8)),
            "email": "b10923003@gemail.yuntech.edu.tw"
        }
        request = self.factory.post(path='/api/account/register/', data=data, format='json')

        view = Register.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(response.data['register'])
        self.assertEqual(response.data['user']['username'], 'test_003')
        logger.info("Complete User Register with non-existing user")

    def test_register_existing_user(self):
        User.objects.create_user(username="existing_user", password=str(secrets.randbits(8)),
                                 email="existinguser@example.com")
        data = {
            "username": "existing_user",
            "password": str(secrets.randbits(8)),
            "email": "existinguser@example.com"
        }
        request = self.factory.post(path='/api/account/register/', data=data, format='json')

        view = Register.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertFalse(response.data['register'])
        self.assertEqual(response.data['message'], 'Duplicate Username or Email')
        logger.info("Complete User Register with existing user")

    def test_logout(self):
        User.objects.create_user(username='test_user', password=str(secrets.randbits(8)))

        request = self.factory.get(path='/api/account/logout/')

        # User SessionMiddleware to deal session
        middleware = SessionMiddleware(SimpleNamespace())
        middleware.process_request(request)
        request.session.save()

        view = LogoutAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"status": "success", "logout": True})
        self.assertNotIn('_auth_user_id', request.session)
        self.assertFalse(request.user.is_authenticated)

        logger.info("Complete test user logout")

    def test_edit_profile_with_username(self):
        User.objects.create_user(username='test_user', password='test_password')
        data = {
            "username": "test_user",
            "password": str(secrets.randbits(8)),
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "email": "test@gmail.com"
        }
        request = self.factory.put(path='/api/account/profile/edit/', data=data)

        view = EditProfileAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(response.data['edit'])

        logger.info("Complete test user edit profile with username")

    def test_edit_profile_without_username(self):
        data = {
            "username": "",
            "password": str(secrets.randbits(8)),
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "email": "test@gmail.com"
        }
        request = self.factory.put(path='/api/account/profile/edit/', data=data)

        view = EditProfileAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data['status'], 'error')
        self.assertFalse(response.data['edit'])

        logger.info("Complete test user edit profile without username")

    def test_list_user(self):
        User.objects.create_user(username='test_user1', password='test_password1')
        User.objects.create_user(username='test_user2', password='test_password2')
        User.objects.create_user(username='test_user3', password='test_password3')
        User.objects.create_user(username='test_user4', password='test_password4')

        request = self.factory.get(path='/api/account/all/')

        view = UserAPIView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        logger.info("Complete test list user")

    def test_oauth_user_register(self):
        data_oauth = {
            "username": "test_oauth_register",
            "password": str(secrets.randbits(8)),
            "email": "test_oauth_register@gemail.yuntech.edu.tw"
        }
        request = self.factory.post(path='/api/account/oauth/register/', data=data_oauth, format='json')

        view = OAuthUserRegisterAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(response.data['register'])
        self.assertEqual(response.data['Identity'], "OAuth User")
        self.assertEqual(response.data['user']['username'], "test_oauth")
        logger.info("Complete OAuth User Register")

    def test_oauth_existing_user_register(self):
        User.objects.create_user(username="test_oauth", password=str(secrets.randbits(8)),
                                 email="test_oauth@gemail.yuntech.edu.tw")
        data = {
            "username": "test_oauth",
            "password": str(secrets.randbits(8)),
            "email": "test_oauth@gemail.yuntech.edu.tw"
        }
        request = self.factory.post(path='/api/account/oauth/register/', data=data, format='json')

        view = OAuthUserRegisterAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['status'], 'failed')
        self.assertEqual(response.data['message'], "Duplicate Username or Email")
        logger.info("Complete OAuth Existing User Register")

    def test_oauth_user_login(self):
        User.objects.create_user(username='test_oauth_login', password=str(secrets.randbits(8)),
                                 email="test_oauth_login@gemail.yuntech.edu.tw")
        data = {
            "email": "test_oauth_login@gemail.yuntech.edu.tw"
        }
        request = self.factory.post(path='/api/account/oauth/login/', data=data, format='json')

        view = OAuthUserLoginAPI.as_view()
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertTrue(response.data['login'])
        self.assertEqual(response.data['Identity'], "OAuth User")
        self.assertEqual(response.data['user']['username'], "test_oauth_login")
        logger.info("Complete OAuth User Login")