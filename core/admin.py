from django.contrib import admin
from .models import Project, Blog, Skill, Contact, Service
from django.contrib.postgres.fields import ArrayField
from django.forms import TextInput



admin.site.register(Project)
admin.site.register(Blog)
admin.site.register(Skill)
admin.site.register(Contact)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')

admin.site.register(Service, ServiceAdmin)