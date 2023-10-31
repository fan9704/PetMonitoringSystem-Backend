# import logging
#
# from django.test import TestCase
# from rest_framework import status
# from rest_framework.test import APIClient
# from api.models import User
#
# logger = logging.getLogger(__name__)
#
#
# class UserIntegrationTest(TestCase):
#
#     def setUp(self):
#         self.client = APIClient()
#         self.exist_username = 'existing_user'
#         self.exist_password = 'existing_password'
#         self.exist_email = 'existinguser@example.com'
#         self.exist_first_name = 'existing_first',
#         self.exist_last_name = 'existing_last'
#         self.exist_user_data = {
#             "username": self.exist_username,
#             "password": self.exist_password,
#             "email": self.exist_email
#         }
#         logger.info("Complete Init User Integration Test")
#
#     def test_register_new_user(self):
#         data = {
#             "username": "b10923003",
#             "password": "b10923003",
#             "email": "b10923003@gemail.yuntech.edu.tw"
#         }
#
#         response = self.client.post('/api/account/register/', data, format='json')
#
#         # Check API Response
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['status'], 'success')
#         self.assertTrue(response.data['register'])
#         self.assertEqual(response.data['user']['username'], 'b10923003')
#
#         # Check database user data is existing
#         self.assertTrue(User.objects.filter(username='b10923003').exists())
#         logger.info("Complete Test Register New User")
#
#     def test_register_existing_user(self):
#         # Create Existing User in Database
#         User.objects.create_user(username=self.exist_username, password=self.exist_password, email=self.exist_email)
#
#         response = self.client.post('/api/account/register/', self.exist_user_data, format='json')
#
#         # Check API Response
#         self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
#         self.assertFalse(response.data['register'])
#         self.assertEqual(response.data['message'], 'Duplicate Username or Email')
#         logger.info("Complete Test Register Existing User")
#
#     def test_logout_user(self):
#         self.user = User.objects.create_user(username=self.exist_username, password=self.exist_password)
#         self.client.login(username=self.exist_username, password=self.exist_password)
#
#         response = self.client.get('/api/account/logout/', format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertNotIn('_auth_user_id', self.client.session)
#         logger.info("Complete Test Logout User")
#
#     def test_edit_profile_success(self):
#         User.objects.create_user(username=self.exist_username, password=self.exist_password, email=self.exist_email)
#
#         data = {
#             "username": self.exist_username,
#             "password": self.exist_password,
#             'first_name': "new_first_name",
#             "last_name": self.exist_last_name,
#             "email": self.exist_email
#         }
#
#         response = self.client.put('/api/account/profile/edit/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["status"], "success")
#         self.assertEqual(response.data["edit"], True)
#         logger.info("Complete Test Edit User Profile Success")
#
#     def test_edit_profile_fail(self):
#         # Create Existing User in Database
#         User.objects.create_user(username=self.exist_username, password=self.exist_password, email=self.exist_email)
#         data = {
#             "username": "",
#             "password": self.exist_password,
#             'first_name': self.exist_first_name,
#             "last_name": self.exist_last_name,
#             "email": self.exist_email
#         }
#         response = self.client.put('/api/account/profile/edit/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
#         self.assertEqual(response.data["status"], "error")
#         self.assertEqual(response.data["edit"], False)
#         logger.info("Complete Test Edit User Profile Failed")
#
#     def test_list_user(self):
#         for i in range(1, 5):
#             User.objects.create_user(username=f'b1092300{i}', password=f'b1092300{i}', email=f'{i}@gmail.com')
#         response = self.client.get('/api/account/user/all/', format='json')
#         self.assertEqual(len(response.data), 4)
#         logger.info("Complete Test List User")
#
#     def test_oauth_non_exist_user_register(self):
#         response = self.client.post('/api/account/oauth/register/', self.exist_user_data, format='json')
#
#         self.assertTrue(response.data['register'])
#         self.assertEqual(response.data['Identity'], "OAuth User")
#         self.assertEqual(response.data["status"], "success")
#         self.assertEqual(response.data["user"]["username"], self.exist_username)
#         logger.info("Complete Test Register OAuth User")
#
#     def test_oauth_non_exist_user_register(self):
#         User.objects.create_user(username=self.exist_username, password=self.exist_password, email=self.exist_email)
#         response = self.client.post('/api/account/oauth/register/', self.exist_user_data)
#
#         self.assertFalse(response.data['register'])
#         self.assertEqual(response.data["status"], "failed")
#         self.assertEqual(response.data["message"], "Duplicate Username or Email")
#         logger.info("Complete Test Register Existing OAuth User")
#
#     def test_oauth_user_login(self):
#         User.objects.create_user(username=self.exist_username, password=self.exist_password, email=self.exist_email)
#         data = {
#             "email": self.exist_email
#         }
#         response = self.client.post('/api/account/oauth/login/', data, format="json")
#
#         self.assertEqual(response.data["status"], "success")
#         self.assertEqual(response.data["Identity"], "OAuth User")
#         self.assertTrue(response.data["login"])
#         self.assertEqual(response.data["user"]["username"], self.exist_username)
#         logger.info("Complete Test Login OAuth User")
