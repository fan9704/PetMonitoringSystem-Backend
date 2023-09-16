import logging

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIRequestFactory

from api.views.loginViews import LoginView

logger = logging.getLogger(__name__)


class LoginAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

    def tearDown(self) -> None:
        User.objects.all().delete()

    def test_login_valid_user(self):
        data = {
            'username': 'test_user',
            'password': 'test_password'
        }

        request = self.factory.post('/api/account/login/', data)
        view = LoginView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_login_invalid_user(self):
        data = {
            'username': 'test_user',
            'password': 'wrong_password'
        }

        request = self.factory.post('/api/account/login/', data)
        view = LoginView.as_view()
        response = view(request)

        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.data, {'detail': 'Invalid credentials'})
