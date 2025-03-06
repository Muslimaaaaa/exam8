from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from ..models import *
from ..serializers import *

class AttendanceLevelApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    pagination_class = PageNumberPagination
    queryset = AttendanceLevel.objects.all().order_by('-id')
    serializer_class = AttendanceLevelSerializer


class AttendanceApi(ModelViewSet):
    permission_classes = [IsAuthenticated]

    pagination_class = PageNumberPagination
    queryset = Attendance.objects.all().order_by('-id')
    serializer_class = AttendanceSerializer
