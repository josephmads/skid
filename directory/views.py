from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Idea, SkidUserDetail, Skill, Material, WorkType

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

class UserListView(generic.ListView):
    model = SkidUserDetail
    template_name = 'directory/user_list.html'
    context_object_name = 'user_list'
    ordering = ['last_name']

def user_detail_view(request, username):
    sud = SkidUserDetail.objects.filter(username__username=username).first() #FIX ME Write Test for when no SUD exists
    context = {
        'sud': sud
    }
    return render(request, 'directory/user_detail.html', context)

def list_skills(request, skill_id):
    """View function lists users by the skills they are tagged with."""
    skill = get_object_or_404(Skill, id=skill_id)
    users = skill.users.all()
    context = {
        'skill_name': skill.skill,
        'users': users
    }
    return render(request, 'directory/user_list.html', context)

def list_materials(request, material_id):
    """View function lists users by the materials they are tagged with."""
    material = get_object_or_404(Material, id=material_id)
    users = material.users.all()
    context = {
        'material_name': material.material,
        'users': users
    }
    return render(request, 'directory/user_list.html', context)

def list_work_type(request, type_id):
    """View function lists users by the type of work they are tagged with."""
    type = get_object_or_404(WorkType, id=type_id)
    users = type.users.all()
    context = {
        'type_name': type.work_type,
        'users': users
    }
    return render(request, 'directory/user_list.html', context)

#IDEA LIST, DETAIL, AND COMMENT

class IdeaListView(generic.ListView):
    queryset = Idea.objects.filter(status='p').order_by('-published')
    template_name = 'directory/idea_list.html'
    context_object_name = 'idea_list'
    

def idea_detail(request, slug):
    idea = Idea.objects.get(slug=slug)
    context = {
        'idea': idea,
    }
    return render(request, 'directory/idea_detail.html', context)