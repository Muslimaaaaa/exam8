from django.db import models

from . import Student
from ..models import *
from .group import Groupm

class AttendanceLevel(models.Model):
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    level = models.ForeignKey(AttendanceLevel, on_delete=models.RESTRICT, name='level')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, name='student' )
    group = models.ForeignKey(Groupm, on_delete=models.RESTRICT, name='group')

    def __str__(self):
        return self.level
