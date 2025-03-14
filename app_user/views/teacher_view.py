from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from ..models import User, Teacher, Group
from ..serializers import TeacherSerializer, UserSerializer, auth_serializer, CreateTeacherSerializer, CourseSerializer, \
    GroupSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination


class TeacherPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class TeacherApiViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = CreateTeacherSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__phone', 'user__full_name']
    pagination_class = TeacherPagination


class WorkerGroupsAPIView(APIView):
    def get(self, request, worker_id):
        try:
            worker = Teacher.objects.get(id=worker_id)

            groups = Group.objects.filter(teacher=worker)

            serializer = GroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Teacher.DoesNotExist:
            return Response({"error": "Worker not found"}, status=status.HTTP_404_NOT_FOUND)




