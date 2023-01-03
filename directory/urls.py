from django.urls import path
from . import views

app_name = 'directory'

urlpatterns = [
    path('', views.directory, name='directory'),
    path('users/', views.UserListView.as_view(), name='users'),
    # path('<slug:slug>/', views.UserDetailView.as_view(), name='user_detail'),
    path('<username>/', views.user_detail_view, name='user_detail'),
    path('skills/<int:skill_id>', views.list_skills, name='skill'),
    path('materials/<int:material_id>', views.list_materials, name='material'),
    path('worktype/<int:type_id>', views.list_work_type, name='work_type'),
]