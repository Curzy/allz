import uuid

from django.test import TestCase

from .models import AllZUser


class AllZUserTestCase(TestCase):

    def test_user_create(self):
        email, username, password = "test@test.com", "username", "password"

        _ = AllZUser.objects.create_user(email, username, password)
        user = AllZUser.objects.get(email=email)

        self.assertTrue(isinstance(user.id, uuid.UUID))
        self.assertEqual(user.email, email)
        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

        first_name, last_name = 'first', 'last'
        user.first_name, user.last_name = first_name, last_name
        user.save()

        user = AllZUser.objects.get(email=email)

        self.assertNotEqual(user.created_at, user.modified_at)
        self.assertEqual(user.first_name, first_name)
        self.assertEqual(user.last_name, last_name)
