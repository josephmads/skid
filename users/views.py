from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView

from .forms import UserUpdateForm, SkidUserDetailUpdateForm
from directory.models import SkidUserDetail

User=get_user_model()

import pprint
# Create your views here.

@login_required()
def profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()
        if user:
            details = SkidUserDetail.objects.filter(username__username=username).first()
            context = {
                'details': details,
                'user': user
            }

            return render(request, 'users/profile.html', context=context)

        # return redirect('users:user_denied')
        raise Exception(redirect('users:user_denied'))
    
    except Exception as err:
        return HttpResponse(str(err), status=406)


@login_required
def edit_profile(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if request.method == 'POST':
            user = request.user
            form = SkidUserDetailUpdateForm(request.POST, instance=user)

            if form.is_valid():
                # user_form = form.save()
                profile = form.save(commit=False)
                profile.user = user
                profile.save()
                breakpoint()

                return redirect('users:profile', profile.username)
                # return HttpResponseRedirect(reverse(''))

        if user:
            form = SkidUserDetailUpdateForm(instance=user)
            context = {
                'form':form
            }

            return render(request, 'users/edit_profile.html', context=context)

        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)


class UserDenied(TemplateView):
    template_name = 'user_denied.html'