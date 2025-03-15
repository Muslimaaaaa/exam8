from django.db import models
from . import Student
from . import Group
from ..models import *

class AttendanceLevel(models.Model):
    """
    davomat, bu model orqali bir talaba necha soat dars qoldirganligini bilib olsa bo'ladi
    """
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

class Attendance(models.Model):
    """
    davomat modelning o'zi
    """
    level = models.ForeignKey(AttendanceLevel, on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    group = models.ForeignKey(Group, on_delete=models.RESTRICT)

    def __str__(self):
        return self.level