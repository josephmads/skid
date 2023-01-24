from django.urls import include, path
from rest_framework import routers
from . import views

# Url Patterns

router = routers.DefaultRouter()
router.register(r'ideas', views.IdeaViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'skills', views.SkillViewSet)
router.register(r'materials', views.MaterialViewSet)
router.register(r'work_types', views.WorkTypeViewSet)

urlpatterns = [
    path('', include(router.urls), name='api'),
    path('api-auth/', include(
        'rest_framework.urls', 
        namespace='rest_framework'
        )),
]