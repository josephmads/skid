from django.test import TestCase

from users.forms import *

# Create your tests here.

class ProfileUpdateFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(
            username='testertim',
            first_name='Tim',
            last_name='Timons',
            email='tim.timons@test.test',
        )

        Profile.objects.filter(id=1).update(
            business_name="Tim's Testing Inc.",
            email_public='tim.public@test.test'
        )

    def test_profile_update_valid_form(self):
        profile = Profile.objects.get(id=1)
        data = {
            'business_name': profile.business_name,
            'email_public': profile.email_public,
            }
        form = ProfileUpdateForm(data=data)
        self.assertTrue(form.is_valid())
        