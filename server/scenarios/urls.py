from django.urls import path, include
from rest_framework.routers import DefaultRouter

from scenarios.infrastructure.views.project_view import ProjectViewSet

projects = DefaultRouter(trailing_slash=False)
projects.register(
    "items",
    ProjectViewSet,
    basename="projects_items",
)

urlpatterns = [
    path("projects/", include(projects.urls)),
]
