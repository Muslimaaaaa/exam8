from rest_framework import serializers

from app_user.models import Student, Parents


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'


class StudentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name','is_activate', 'phone', 'group', 'organization', 'descriptions']

