from rest_framework import viewsets
from ..models import Group
from ..serializers.group_serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

