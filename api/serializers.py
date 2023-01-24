from users.models import *
from rest_framework import serializers


# SERIALIZERS

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]

class IdeaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Idea
        fields = [
            'author',
            'title',
            'text',
            'published',
            'skills',
            'materials',
            'type_of_work',
            'status',
        ]

class SkillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill']

class MaterialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Material
        fields = ['material']

class WorkTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorkType
        fields = ['work_type']
