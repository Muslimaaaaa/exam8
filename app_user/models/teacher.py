from django.db import models
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .auth import User

class Course(models.Model):
    """o'quv markazda o'qitiladigan fanlar"""
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"ID: {self.id} | {self.title}"

class Departments(models.Model):
    """ Ishchilarning darajasini belgilash uchun model"""
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__phone', 'user__full_name']

    def __str__(self):
        return self.title

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departments = models.ManyToManyField(Departments, related_name='teacher')
    course = models.ManyToManyField(Course, related_name='teacher')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id} | {self.user.phone}"