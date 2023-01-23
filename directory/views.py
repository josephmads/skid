from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from users.models import Idea, Profile, Skill, Material, WorkType

User=get_user_model()

# Create your views here.

def home(request):
    """View function for the home page."""
    return render(request, 'directory/home.html')
 
def directory(request):
    """
    View function landing page for the directory side of the site.
    Lists links to filter users and ideas.
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

def user_list_view(request):
    """View function lists all non-staff users and paginates results."""
    all_users = User.objects.filter(is_staff=False).order_by('last_name')
    paginator = Paginator(all_users, 5)
    page_number = request.GET.get('page')

    users = paginator.get_page(page_number)

    context = {
        'users': users,
    }
    return render(request, 'directory/user_list.html', context)

def user_detail_view(request, username):
    """View function diplays details of user."""
    user = User.objects.filter(username=username)
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
    """View function lists all ideas and paginates results."""
    all_ideas = Idea.objects.filter(status='p').order_by('-published')
    paginator = Paginator(all_ideas, 5)
    page_number = request.GET.get('page')

    idea_list = paginator.get_page(page_number)

    context = {
        'idea_list': idea_list
    }
    return render(request, 'directory/idea_list.html', context)

def idea_detail(request, slug):
    """View function displays details of ideas."""
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
    