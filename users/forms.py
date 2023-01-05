from django import forms
from django.contrib.auth import get_user_model
from directory.models import SkidUserDetail

User=get_user_model()


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',]


class SkidUserDetailUpdateForm(forms.ModelForm):

    class Meta:
        model = SkidUserDetail
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
            'skills',
            'materials',
            'type_of_work',
        ]

        labels = {
            'type_of_work': 'Type of Work',
        }