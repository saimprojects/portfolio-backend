from rest_framework import serializers
from .models import Project, Blog, Skill, Contact, Service

class ProjectSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()  # ✅ Yeh zaroori hai!

    class Meta:
        model = Project
        fields = '__all__'

    def get_image(self, obj):
        return obj.image.url

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'