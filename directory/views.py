from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.views import generic

from itertools import chain
from django.db.models import Q

from users.models import Idea, Profile, Skill, Material, WorkType

User=get_user_model()

# Create your views here.

def home(request):
    """View function for the home page."""
    return render(request, 'directory/home.html')
 
def directory(request):
    """
    View function landing page for the directory side of the site.
    Lists links to filter users.
    """
    skills = Skill.objects.all()
    materials = Material.objects.all()
    worktype = WorkType.objects.all()
    context = {
        'skills': skills,
        'materials': materials,
        'worktype': worktype,
    }
    return render(request, 'directory/directory.html', context)

#USER LIST AND DETAIL

# def user_list_view(request):
#     users = User.objects.filter(is_staff=False).order_by('-last_name')
#     profiles = Profile.objects.all()
#     context = {
#         'users': users,
#         'profiles': profiles,
#     }
#     return render(request, 'directory/user_list.html', context)

combined_user_list = []

def user_list_view(request):
    users_not_staff = User.objects.filter(is_staff=False).order_by('-last_name')
    for user in users_not_staff:
        profile = Profile.objects.filter(user_id=user.id)
        skills = Skill.objects.filter(profile__in=profile)
        materials = Material.objects.filter(profile__in=profile)
        work_type = WorkType.objects.filter(profile__in=profile)
        # setattr(user, 'profile', profile)
        user.profile = profile
        user.skills = skills
        user.materials = materials
        user.work_type = work_type
        combined_user_list.append(user)

    # breakpoint()

    context = {'combined_user_list': combined_user_list}
    return render(request, 'directory/user_list.html', context)

def user_detail_view(request, username):
    user = User.objects.filter(username=username).first()
    profile = Profile.objects.filter(user_id__username=username).first()
    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'directory/user_detail.html', context)

def list_skills(request, skill_id):
    """View function lists users by the skills they are tagged with."""
    skill = get_object_or_404(Skill, id=skill_id)
    users = skill.profile.all()
    context = {
        'skill_name': skill.skill,
        'users': users,
    }
    return render(request, 'directory/user_list.html', context)

def list_materials(request, material_id):
    """View function lists users by the materials they are tagged with."""
    material = get_object_or_404(Material, id=material_id)
    users = material.profile.all()
    context = {
        'material_name': material.material,
        'users': users
    }
    return render(request, 'directory/user_list.html', context)

def list_work_type(request, type_id):
    """View function lists users by the type of work they are tagged with."""
    type = get_object_or_404(WorkType, id=type_id)
    users = type.profile.all()
    context = {
        'type_name': type.work_type,
        'users': users
    }
    return render(request, 'directory/user_list.html', context)

#IDEA LIST, DETAIL, AND COMMENT


def idea_list(request):
    idea_list = Idea.objects.filter(status='p').order_by('-published')
    context = {
        'idea_list': idea_list
    }
    return render(request, 'directory/idea_list.html', context)

def idea_detail(request, slug):
    idea = Idea.objects.get(slug=slug)
    context = {
        'idea': idea,
    }
    return render(request, 'directory/idea_detail.html', context)

def list_idea_skills(request, skill_id):
    """View function lists ideas by the skills they are tagged with."""
    skill = get_object_or_404(Skill, id=skill_id)
    ideas = skill.idea.all()
    context = {
        'skill_name': skill.skill,
        'ideas': ideas,
    }
    return render(request, 'directory/idea_list.html', context)

def list_idea_materials(request, material_id):
    """View function lists ideas by the materials they are tagged with."""
    material = get_object_or_404(Material, id=material_id)
    ideas = material.idea.all()
    context = {
        'material_name': material.material,
        'ideas': ideas
    }
    return render(request, 'directory/idea_list.html', context)

def list_idea_work_type(request, type_id):
    """View function lists ideas by the type of work they are tagged with."""
    type = get_object_or_404(WorkType, id=type_id)
    ideas = type.idea.all()
    context = {
        'type_name': type.work_type,
        'ideas': ideas
    }
    return render(request, 'directory/idea_list.html', context)