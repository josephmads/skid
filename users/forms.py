from django import forms
from django.contrib.auth import get_user_model
from .models import Profile, Skill

User=get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super(ProfileUpdateForm, self).__init__(*args, **kwargs)
    #     if self.instance:\
    #         self.initial['first_name'] = Profile.objects.filter()

    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'business_name',
            'email_address',
            'phone_number',
            'address',
            'city',
            'state_province',
            'zip_code',
            'country',
            'about',
            'skills',
            'materials',
            'type_of_work',
        ]

        labels = {
            'type_of_work': 'Type of Work',
        }