from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import PageNumberPagination
from ..models import User, Student
from ..serializers import CreateStudentSerializer, ParentsSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

from rest_framework.pagination import PageNumberPagination

class StudentPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class StudentApiViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = CreateStudentSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__phone', 'user__full_name']
    pagination_class = StudentPagination

class ParentsApiView(APIView):
    permission_classes = [IsAdminUser]
    pagination_class = PageNumberPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['user__phone', 'user__full_name']
    @swagger_auto_schema(request_body=ParentsSerializer)
    def post(self, request):
        serializer = ParentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'status': True, 'detail': "Parents created"}, status=status.HTTP_201_CREATED)
        return Response({'status': False, 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)