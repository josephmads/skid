from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('add-skill/', views.add_skill, name='add_skill'),
    path('add-material/', views.add_material, name='add_material'),
    path('add-work-type/', views.add_work_type, name='add_work_type'),
    path('<str:username>/', views.profile, name='profile'),
    path('<str:username>/edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/create-idea/', views.create_idea, name='create_idea'),
    path('<str:username>/edit-idea/<slug:slug>', views.edit_idea, name='edit_idea'),
    path('<str:username>/delete-idea/<slug:slug>', views.delete_idea, name='delete_idea'),
    path('<str:username>/view-ideas/', views.view_ideas, name='view_ideas'),
    
]