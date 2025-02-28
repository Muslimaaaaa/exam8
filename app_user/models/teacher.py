from django.db import models
from app_user.models import User, Course

class Departments(models.Model):
    title = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departments = models.ManyToManyField(Departments, related_name='teacher')
    course = models.ManyToManyField(Course, related_name='teacher')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    descriptions = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.user

