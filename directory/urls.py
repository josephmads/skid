from django.urls import path
from . import views

app_name = 'directory'

urlpatterns = [
    path('', views.directory, name='directory'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('<username>/', views.user_detail_view, name='user_detail'),
    path('ideas/', views.IdeaListView.as_view(), name='ideas'),
    # path('ideas/', views.idea_list, name='ideas'),
    path('ideas/<slug:slug>/', views.idea_detail, name='idea_detail'),
    path('user-skills/<int:skill_id>', views.list_skills, name='user_skill'),
    path('user-materials/<int:material_id>', views.list_materials, name='user_material'),
    path('user-worktype/<int:type_id>', views.list_work_type, name='user_work_type'),
    path('idea-skills/<int:skill_id>', views.list_idea_skills, name='idea_skill'),
    path('idea-materials/<int:material_id>', views.list_idea_materials, name='idea_material'),
    path('idea-worktype/<int:type_id>', views.list_idea_work_type, name='idea_work_type'),
]