from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, TeacherViewApi, TeacherViewSet
from .views.group_view import GroupViewSet

router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
urlpatterns = [
    path('', include(router.urls)),

]
