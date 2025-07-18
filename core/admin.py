from django.contrib import admin
from .models import Project, Blog, Skill, Contact, Service
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from django.db import models

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Service, ServiceAdmin)
