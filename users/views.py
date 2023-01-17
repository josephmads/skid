from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import TemplateView
from django.forms.models import model_to_dict

from .forms import *
from .models import Profile

User=get_user_model()

# Create your views here.

class UserDenied(TemplateView):
    template_name = 'user_denied.html'

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
                    messages.success(request, "Profile updated successfully.")
                
                    return redirect('users:profile', username)

                else:
                    messages.warning(request, "Please correct the error below.")

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


@login_required
def create_idea(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            if request.method == 'POST':
                form = IdeaForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Idea created successfully.')
                    
                    return redirect('users:profile', username)

                else:
                    print(form.errors)

            elif request.method == 'GET':
                author_field = {'author': user}
                form = IdeaForm(instance=user, initial=author_field)
              
                context = {
                    'form': form
                }
                return render(request, 'users/create_idea.html', context=context)

        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)


@login_required
def edit_idea(request, username, slug):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            # Queries idea for existing data
            idea_data = Idea.objects.filter(slug=slug).first()

            if request.method == 'POST':
                form = IdeaForm(request.POST, instance=idea_data)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Idea edited successfully.')

                return redirect('users:view_ideas', username)

            elif request.method == 'GET':
                # Converts data into dict to be passed the initial field
                existing_data = model_to_dict(idea_data)
                idea_form = IdeaForm(instance=user, initial=existing_data)

                context = {
                    'idea_form': idea_form
                    }

                return render(request, 'users/edit_idea.html', context=context)
        
        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)

@login_required
def delete_idea(request, username, slug):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            # Queries idea for existing data
            idea_data = Idea.objects.filter(slug=slug).first()

            if request.method == 'POST':
                idea_data.delete()
                messages.success(request, 'Idea deleted successfully.')

                return redirect('users:view_ideas', username)

            elif request.method == 'GET':
                context = {'idea_data': idea_data}
                
                return render(request, 'users/delete_idea.html', context)
        
        raise Exception("You don't belong here. GO AWAY!")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)

@login_required
def view_ideas(request, username):
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId, username=username).first()

        if user:
            ideas = Idea.objects.filter(author=user)
            context = {
                'ideas': ideas,
                'user': user,
            }
            return render(request, 'users/view_ideas.html', context=context)

        raise Exception(f"You shouldn't be here.")
    
    except Exception as err:
        return HttpResponse(str(err), status=406)

@login_required
def add_skill(request):
    skills = Skill.objects.all().order_by('skill')
    form = SkillForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Skill added.')

        return redirect('users:add_skill')

    elif request.method == 'GET':
        context = {
            'skills': skills,
            'form': form,
        }

        return render(request, 'users/add_skill.html', context=context)

@login_required
def add_material(request):
    materials = Material.objects.all().order_by('material')
    form = MaterialForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Material added.')

        return redirect('users:add_material')

    elif request.method == 'GET':
        context = {
            'materials': materials,
            'form': form,
        }

        return render(request, 'users/add_material.html', context=context)

@login_required
def add_work_type(request):
    work_types = WorkType.objects.all().order_by('work_type')
    form = WorkTypeForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Work type added.')

        return redirect('users:add_work_type')

    elif request.method == 'GET':
        context = {
            'work_types': work_types,
            'form': form,
        }

        return render(request, 'users/add_work_type.html', context=context)