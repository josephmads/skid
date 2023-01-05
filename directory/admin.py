from django.contrib import admin
from .models import Idea, Skill, Material, WorkType, SkidUserDetail

# Register your models here.

class SkidUserDetailAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'first_name', 
        'last_name', 
        'business_name', 
        'email_address',
    )
    search_fields = ['username', 'first_name', 'last_name']

class IdeaAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'title',
        'published',
        'updated',
    )
    list_filter = ('status',)
    search_fields = ['username', 'title', 'text']

admin.site.register(Skill)
admin.site.register(Material)
admin.site.register(WorkType)
admin.site.register(SkidUserDetail, SkidUserDetailAdmin)
admin.site.register(Idea, IdeaAdmin)