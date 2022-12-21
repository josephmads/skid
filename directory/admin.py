from django.contrib import admin
from .models import Skill, Material, WorkType, SkidUserDetail

# Register your models here.

class SkidUserDetailAdmin(admin.ModelAdmin):
    list_display = (
        'username', 
        'first_name', 
        'last_name', 
        'business_name', 
        'email_address',
    )
    exclude = ('slug',)

admin.site.register(Skill)
admin.site.register(Material)
admin.site.register(WorkType)
admin.site.register(SkidUserDetail, SkidUserDetailAdmin)