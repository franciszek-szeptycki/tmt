from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase


class CreateUserCommandTestCase(TestCase):

    def test_create_user_noinput(self):
        call_command('create_user', '--noinput', stdout=StringIO())

        user = User.objects.get(username='johndoe')
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('password'))

    def test_create_user_with_username_password(self):
        call_command('create_user', '--username=testuser', '--password=secret', stdout=StringIO())

        user = User.objects.get(username='testuser')
        self.assertIsNotNone(user)
        self.assertTrue(user.check_password('secret'))

    def test_create_user_missing_username(self):
        call_command('create_user', '--password=secret', stdout=StringIO())
        self.assertEqual(User.objects.all().count(), 0)

    def test_create_user_missing_password(self):
        call_command('create_user', '--username=testuser', stdout=StringIO())
        self.assertEqual(User.objects.all().count(), 0)

