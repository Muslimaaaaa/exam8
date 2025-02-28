from django.db import models
from app_user.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    group = models.ManyToManyField(User)
