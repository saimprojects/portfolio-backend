from django.contrib import admin
from .models import Project, Blog, Skill, Contact, Service
from django import forms
from ckeditor.widgets import CKEditorWidget

# Project Form
class ProjectAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Project
        fields = '__all__'

# Blog Form
class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Blog
        fields = '__all__'

# Project Admin
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm

# Blog Admin
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

# Service Admin (jo pehle tha wo same rakh lo)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')


# Register Models
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Skill)
admin.site.register(Contact)
admin.site.register(Service, ServiceAdmin)
