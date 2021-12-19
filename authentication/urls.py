from django.urls import path, include
from authentication.api.v1.views.client import ClientViewSet
from authentication.models import Client


urlpatterns = [
    path("clients/", ClientViewSet.as_view()),
]
