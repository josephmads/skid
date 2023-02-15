from django.contrib import admin
from .models import *

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 
        'business_name', 
        'email_public',
    )

class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'published',
        'updated',
    )
    list_filter = ('status',)
    search_fields = ['title', 'text']

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'commenter',
        'text',
        'idea',
        'created_on',
    )
    list_filter = ('created_on',)
    search_fields = ('commenter', 'idea',)

admin.site.register(Skill)
admin.site.register(Material)
admin.site.register(WorkType)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Idea, IdeaAdmin)
admin.site.register(Comment, CommentAdmin)
