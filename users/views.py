from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import ProfileUpdateForm
from .models import Profile, Skill

User=get_user_model()

# Create your views here.

@login_required()
def profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()
        if user:
            details = Profile.objects.filter(username__username=username).first()
            context = {
                'details': details,
                'user': user
            }

            return render(request, 'users/profile.html', context=context)

        # return redirect('users:user_denied')
        raise Exception(redirect('users:user_denied'))
    
    except Exception as err:
        return HttpResponse(str(err), status=406)

from django.forms.models import model_to_dict
@login_required()
def edit_profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if request.method == 'POST':
            form = ProfileUpdateForm(
                request.POST, 
                instance=request.user.profile,
                )

            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('users:profile', profile.username)

        elif user:
            # form = ProfileUpdateForm(instance=user)
            qs = Profile.objects.filter(title=item.title)

            if qs.exists():
                qs_dict = model_to_dict(qs) # {id:1,'estimate':'some-estimate-data','logic':'some-logic-data'}

            existing_data = {

            }
            form = ProfileUpdateForm(initial=existing_data)
            context = {
                'form':form
            }

            return render(request, 'users/edit_profile.html', context=context)

        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)

# @login_required
# def profile(request):
#     return render(request, 'users/profile.html')


class UserDenied(TemplateView):
    template_name = 'user_denied.html'