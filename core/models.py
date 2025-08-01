from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django_ckeditor_5.fields import CKEditor5Field

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = CKEditor5Field('Description', config_name='extends')
    image = CloudinaryField('image', folder='projects')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  # Save first to get self.id
            self.slug = f"{self.id}-{slugify(self.title)}"
            return super().save(update_fields=['slug'])  # Save again only for slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = CKEditor5Field('Content', config_name='extends')
    published_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            super().save(*args, **kwargs)  # Save first to get self.id
            self.slug = f"{self.id}-{slugify(self.title)}"
            return super().save(update_fields=['slug'])  # Save again only for slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField()  # 1-100%

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    features = models.TextField(blank=True)
    price = models.CharField(max_length=50)  # e.g., "$150", "Starting from $1200"
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
