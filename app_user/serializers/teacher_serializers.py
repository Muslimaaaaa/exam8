from rest_framework import serializers
from app_user.models import Course
from ..models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']

class TeacherSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    class Meta:
        model = Teacher
        fields = ['id','full_name', 'descriptions']


class TeacherGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['full_name', 'descriptions']