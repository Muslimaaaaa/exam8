from rest_framework import serializers
from ..models import Attendance, AttendanceLevel
# attendance modeli uchun serializers
class AttendanceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceLevel
        fields = '__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'level', 'level_id', 'created', 'updated', 'student', 'group']
