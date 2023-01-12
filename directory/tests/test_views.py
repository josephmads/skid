from django.test import TestCase
from django.urls import reverse

from users.models import *

# Create your tests here.

class UserListViewTest(TestCase):

    # def setUpTestData(cls):
    #     pass

    def test_view_url_exists_at_location(self):
        response = self.client.get('/directory/users/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accesible_by_name(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)