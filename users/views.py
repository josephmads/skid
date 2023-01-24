from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import *
from .models import Profile

User=get_user_model()

# BASE VIEWS

class HomePage(TemplateView):
    """Class based view diplays the SKID homepage."""
    template_name = 'home.html'

class Credits(TemplateView):
    """Class based view diplays the credits page."""
    template_name = 'credits.html'

# USER APP VIEWS

@login_required()
def profile(request, id):
    """View function displays user profile."""
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            profile = Profile.objects.filter(user_id__id=id).first()
            context = {
                'profile': profile,
                'user': user,
            }
            return render(request, 'users/profile.html', context)

        raise Exception("users/views.py profile()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')
        

@login_required()
def edit_profile(request, id):
    """
    View function displays form to edit user profile. Dynamically
    prepopulates the form with previously saved data.
    """
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            if request.method == 'POST':
                user_form = UserUpdateForm(request.POST, instance=request.user)
                profile_form = ProfileUpdateForm(request.POST, instance=request.user.profile)

                if user_form.is_valid() and profile_form.is_valid():
                    user_form.save()
                    profile_form.save()
                    messages.success(request, "Profile updated successfully.")
                
                    return redirect('users:profile', id)

                else:
                    messages.warning(request, "Please correct the error below.")

            elif request.method == 'GET':
                # Queries user's profile for existing data
                profile_data = Profile.objects.filter(user_id__id=id).first()
                # Converts data into dict to be passed the initial field
                existing_data = model_to_dict(profile_data)

                user_form = UserUpdateForm(instance=request.user)
                profile_form = ProfileUpdateForm(instance=user, initial=existing_data)

                context = {
                    'user_form': user_form,
                    'profile_form': profile_form,
                }
                return render(request, 'users/edit_profile.html', context=context)

        raise Exception("users/views.py edit_profile()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def create_idea(request, id):
    """
    View function displays form for user to create Idea. Prepopulates 
    'author' field to connect Idea to user.
    """
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            if request.method == 'POST':
                form = IdeaForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Idea created successfully.')
                    
                    return redirect('users:profile', id)

                else:
                    print(form.errors)

            elif request.method == 'GET':
                author_field = {'author': user}
                form = IdeaForm(instance=user, initial=author_field)
              
                context = {
                    'form': form
                }
                return render(request, 'users/create_idea.html', context=context)

        raise Exception("users/views.py create_idea()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def edit_idea(request, id, slug):
    """
    View function displays form to edit Idea. Dynamically prepopulates form
    with previously saved data.
    """
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            # Queries idea for existing data
            idea_data = Idea.objects.filter(slug=slug).first()

            if request.method == 'POST':
                form = IdeaForm(request.POST, instance=idea_data)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Idea edited successfully.')

                return redirect('users:view_ideas', id)

            elif request.method == 'GET':
                # Converts data into dict to be passed the initial field
                existing_data = model_to_dict(idea_data)
                idea_form = IdeaForm(instance=user, initial=existing_data)

                context = {
                    'idea_form': idea_form
                    }

                return render(request, 'users/edit_idea.html', context=context)
        
        raise Exception("users/views.py edit_idea()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def delete_idea(request, id, slug):
    """View function displays form to allow user to delete Idea."""
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            # Queries idea for existing data
            idea_data = Idea.objects.filter(slug=slug).first()

            if request.method == 'POST':
                idea_data.delete()
                messages.success(request, 'Idea deleted successfully.')

                return redirect('users:view_ideas', id)

            elif request.method == 'GET':
                context = {'idea_data': idea_data}
                
                return render(request, 'users/delete_idea.html', context)
        
        raise Exception("users/views.py delete_idea()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def view_ideas(request, id):
    """View function displays table of users Ideas."""
    try:
        userId = int(request.session["_auth_user_id"])
        user = User.objects.filter(id=userId).first()

        if user:
            ideas = Idea.objects.filter(author=user)
            context = {
                'ideas': ideas,
            }
            return render(request, 'users/view_ideas.html', context=context)

        raise Exception("users/views.py view_ideas()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def add_skill(request):
    """View function displays form for user to add Skill to table of skills."""
    try:
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
        
        raise Exception("users/views.py add_skill()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def add_material(request):
    """
    View function displays form for user to add Material to table of materials.
    """
    try:
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

        raise Exception("users/views.py add_material()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')


@login_required
def add_work_type(request):
    """
    View function displays form for user to add Work Type to table of 
    work types.
    """
    try:
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

        raise Exception("users/views.py add_work_type()")
    
    except Exception as err:
        # print("ERROR: ", str(err), file=sys.stderr)
        print("ERROR: ", str(err))
        context = {'error': str(err)}
        return render(request, 'error_page.html', context, content_type='text/html')
