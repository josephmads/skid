from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

# Create your tests here.

class UserProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username='tim', 
            first_name='Tim', 
            last_name='Timons', 
            password='te3hjsf82Dst'
            )

    def test_logged_in_profile_uses_correct_template(self):
        login = self.client.login(username='tim', password='te3hjsf82Dst')
        response = self.client.get(reverse('users:profile', kwargs={'username': 'tim'}))
        self.assertEqual(str(response.context['user']), 'tim')
        self.assertEqual(response.status_code, 200)