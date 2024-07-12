from rest_framework import serializers
from scenarios.infrastructure.models.directory import Directory


class DirectorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Directory
        fields = ['id', 'name', 'children', 'parent']

    def get_children(self, obj):
        children = obj.children.all()
        return DirectorySerializer(children, many=True).data
