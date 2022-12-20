from django.urls import path
from . import views

app_name = 'directory'

urlpatterns = [
    path('', views.directory, name='directory'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('<slug:slug>', views.UserDetailView.as_view(), name='user_detail'),
]