from rest_framework import viewsets, mixins
from rest_framework.response import Response

from scenarios.infrastructure.models.directory import Directory
from scenarios.infrastructure.serializers.directory_serializer import DirectorySerializer


class DirectoryView(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin
):
    queryset = Directory.objects.all()
    serializer_class = DirectorySerializer

    def list(self, request, *args, **kwargs):
        root_dirs = Directory.objects.get_root_directories()
        serializer = DirectorySerializer(root_dirs, many=True)
        return Response(serializer.data)
