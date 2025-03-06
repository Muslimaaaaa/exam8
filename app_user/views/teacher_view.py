from app_user.models import Teacher
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

from app_user.serializers import UserSerializer
from app_user.serializers.teacher_serializers import TeacherSerializer, TeacherGetSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherViewApi(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=TeacherSerializer)
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # user_data = request.data.get('user', {})
        # user_serializer = UserSerializer(data=user_data)
        # if user_serializer.is_valid():
        #     user = user_serializer.save()


    def get(self, request):
        teachers = Teacher.objects.all().order_by("id")
        serializer = TeacherGetSerializer(teachers, many=True)
        return Response(data=serializer.data)

class TeacherApiViewId(APIView):
    @swagger_auto_schema(request_body=TeacherGetSerializer)
    def get(self, request, pk):
        try:
            user = Teacher.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def put(self, request, pk):
        try:
            teacher = Teacher.objects.get(id=pk)
            serializer = TeacherGetSerializer(teacher, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def patch(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            serializer = TeacherGetSerializer(teacher, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def delete(self, request, pk):
        try:
            teacher = Teacher.objects.get(pk=pk)
            teacher.delete()
            return Response(data={"message": f"{pk} delete student"})
        except Exception as e:
            return Response(data={'error': e})

