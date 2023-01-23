from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from directory.views import *

# Create your tests here.

class UserListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user([
            User(username='tim', first_name='Tim', last_name='Timons'),
            User(username='tina', first_name='Tina', last_name='Tester'),
            User(username='dj', first_name='DJ', last_name='Ango'),
            User(username='jim', first_name='Jim', last_name='Craig'),
            User(username='joe', first_name='Joe', last_name='Madsen'),
            User(username='pablo', first_name='Pablo', last_name='Hidalgo'),
        ])

    def test_users_view_url_exists_at_location(self):
        response = self.client.get('/directory/users/')
        self.assertEqual(response.status_code, 200)

    def test_users_view_url_accesible_by_name(self):
        response = self.client.get(reverse('directory:users'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_template_content(self):
        response = self.client.get(reverse('directory:users'))
        self.assertContains(response, "<h2>All Users</h2>")
        self.assertContains(response, "dj")