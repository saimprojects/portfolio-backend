from rest_framework import viewsets
from .models import Project, Blog, Skill, Contact, Service
from .serializers import ProjectSerializer, BlogSerializer, SkillSerializer, ContactSerializer, ServiceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'  # ✅ this is key

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'slug'  # ✅ Set to use slug for detail view

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('-submitted_at')
    serializer_class = ContactSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all().order_by('created_at')
    serializer_class = ServiceSerializer