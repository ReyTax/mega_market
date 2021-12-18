from django.urls import path, include
from authentication.api.v1.views.views import get_clients

urlpatterns = [
    path('clients/', get_clients),
]
