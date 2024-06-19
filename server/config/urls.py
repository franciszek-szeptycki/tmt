from django.http import HttpResponse
from django.urls import path, include

urlpatterns = [
    path('users/', include('users.urls')),
    path('', lambda request: HttpResponse("OK", status=200)),
    path('scenarios/', include('scenarios.urls')),
]
