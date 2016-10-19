import uuid

from django.test import TestCase
from django.test.client import RequestFactory

from .models import AllZUser
from .views import IndexView


class AllZUserTestCase(TestCase):

    # FIXME: add facebook social auth test
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


class IndexPageTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_index_page_response(self):
        request = self.factory.get('/')
        response = IndexView.as_view()(request)
        self.assertEqual(response.status_code, 200)
