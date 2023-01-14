from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from django.forms.models import model_to_dict

from .forms import ProfileUpdateForm, UserUpdateForm
from .models import Profile

User=get_user_model()

# Create your views here.

@login_required()
def profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            profile = Profile.objects.filter(user_id__username=username).first()
            context = {
                'profile': profile,
                'user': user,
            }
            return render(request, 'users/profile.html', context=context)

        # return redirect('users:user_denied')
        raise Exception(redirect('users:user_denied'))
    
    except Exception as err:
        return HttpResponse(str(err), status=406)


@login_required()
def edit_profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            if request.method == 'POST':
                user_form = UserUpdateForm(request.POST, instance=request.user)
                profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                
                    return redirect('users:profile', username)

            elif request.method == 'GET':
                # Queries user's profile for existing data
                profile_data = Profile.objects.filter(user_id__username=username).first()
                # Converts data into dict to be passed the initial field
                existing_data = model_to_dict(profile_data)

                user_form = UserUpdateForm(instance=request.user)
                profile_form = ProfileUpdateForm(instance=user, initial=existing_data)

                context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                }
                return render(request, 'users/edit_profile.html', context=context)

        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)



class UserDenied(TemplateView):
    template_name = 'user_denied.html'