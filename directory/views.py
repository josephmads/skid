from django.shortcuts import render
from django.views import generic

from .models import SkidUserDetail

# Create your views here.

def directory(request):
    """View function landing page for the directory side of the site."""
    return render(request, 'directory/directory.html')

class UserListView(generic.ListView):
    model = SkidUserDetail
    template_name = 'directory/user_list.html'
    context_object_name = 'user_list'
    ordering = ['-last_name']

class UserDetailView(generic.DetailView):
    model = SkidUserDetail
    template_name = 'directory/user_detail.html'
    context_object_name = 'sud'

# def user_detail(request, slug):
#     sud = SkidUserDetail.objects.get(slug=slug)
#     context = {'sud': sud}
#     return render(request, 'directory/user_detail.html', context)