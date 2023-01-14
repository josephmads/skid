from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User=get_user_model()

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)

    class Meta: 
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'business_name',
            'email_public',
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