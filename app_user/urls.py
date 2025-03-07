from django.urls import path, include
from .views.teacher_view import TeacherApiView
from .views.student_view import StudentApiView
from .views import WorkerGroupsAPIView
urlpatterns = [
    path("workers/create/", TeacherApiView.as_view(), name='teacher-api'),
    path("student/create/", StudentApiView.as_view(), name='studnet-api'),
    path('teachers/<int:teacher_id>/', TeacherApiView.as_view(), name='teacher-update'),
    path('students/<int:student_id>/', StudentApiView.as_view(), name='student-update'),
]

