from django.shortcuts import render
from users.models import *
from rest_framework import permissions, viewsets
from .serializers import *

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Users to be viewed."""
    queryset = User.objects.filter(is_staff=False).order_by('last_name')
    serializer_class = UserSerializer
    http_method_names = ['get', 'head',]
    permission_classes = [permissions.IsAuthenticated]

class IdeaViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Ideas to be viewed."""
    queryset = Idea.objects.all().order_by('-published')
    serializer_class = IdeaSerializer
    http_method_names = ['get', 'head',]
    permission_classes = [permissions.IsAuthenticated]

class SkillViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Skills to be viewed or edited."""
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [permissions.IsAuthenticated]

class MaterialViewSet(viewsets.ModelViewSet):
    """API endpoint that allows Materials to be viewed or edited."""
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAuthenticated]

class WorkTypeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows WorkTypes to be viewed or edited."""
    queryset = WorkType.objects.all()
    serializer_class = WorkTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
