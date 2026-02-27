from rest_framework.generics import ListAPIView
from .models import Project
from .serializers import ProjectSerializer
from rest_framework.permissions import AllowAny

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]