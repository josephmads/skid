from allauth.account.forms import SignupForm
from django import forms
from django.contrib.auth import get_user_model

from .models import *

User=get_user_model()

# Forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
 
    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

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

class IdeaForm(forms.ModelForm): 

    class Meta:
        model = Idea
        widgets = {
            'author': forms.HiddenInput(),
            'slug': forms.HiddenInput()
            }

        fields = [
            'author',
            'title',
            'slug',
            'text',
            'skills',
            'materials',
            'type_of_work',
            'status'
        ]

class SkillForm(forms.ModelForm):
    skill = forms.CharField(required=False)

    class Meta:
        model = Skill
        fields= ['skill']

class MaterialForm(forms.ModelForm):
    material = forms.CharField(required=False)

    class Meta:
        model = Material
        fields= ['material']

class WorkTypeForm(forms.ModelForm):
    work_type = forms.CharField(required=False)

    class Meta:
        model = WorkType
        fields= ['work_type']
        