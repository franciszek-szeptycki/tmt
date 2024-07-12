from django.urls import path, include
from rest_framework.routers import DefaultRouter

from scenarios.infrastructure.views.directory_view import DirectoryView

directories = DefaultRouter()
directories.register(r'items', DirectoryView)

urlpatterns = [
    path('directories/', include(directories.urls)),
]
