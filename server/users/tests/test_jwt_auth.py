from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SimpleJWTAuthTest(APITestCase):
    def setUp(self):
        self.user_data = {'username': 'testuser', 'password': 'testpassword'}
        self.user = User.objects.create_user(username=self.user_data['username'], password=self.user_data['password'])

    def test_login(self):
        url = reverse('token_obtain_pair')
        data = {'username': self.user_data['username'], 'password': self.user_data['password']}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
