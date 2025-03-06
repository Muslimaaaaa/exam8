from ..models import Student
from ..serializers.student_serializers import StudentSerializer, StudentGetSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentViewApi(APIView):
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(request_body=StudentSerializer)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        students = Student.objects.all().order_by("-id")
        serializer = StudentGetSerializer(students, many=True)
        return Response(data=serializer.data)

class StudentApiViewId(APIView):
    @swagger_auto_schema(request_body=StudentGetSerializer)
    def get(self, request, pk):
        try:
            teacher = Student.objects.get(pk=pk)
            serializer = StudentGetSerializer(teacher)
            return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            serializer = StudentGetSerializer(student, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def patch(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentGetSerializer(student, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(data=serializer.data)
        except Exception as e:
            return Response(data={'error': e})

    def delete(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response(data={"message": f"{pk} delete student"})
        except Exception as e:
            return Response(data={'error': e})