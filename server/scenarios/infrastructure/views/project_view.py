from rest_framework.viewsets import ModelViewSet

from scenarios.infrastructure.models.project_model import Project
from scenarios.infrastructure.serializers.project_serializer import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
