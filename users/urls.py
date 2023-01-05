from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('<username>/edit/', views.edit_profile, name='edit_profile'),
    path('userdenied/', views.UserDenied.as_view(), name='user_denied'),
]