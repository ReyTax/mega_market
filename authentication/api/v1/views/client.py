from django.http import response
from authentication.models import Client

from rest_framework import mixins, viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.generic import View
from django.core.serializers import serialize


class ClientViewSet(View):
    def get(self, request, *args, **kwargs):

        qs = Client.objects.all()
        json_data = serialize("json", qs, fields=(
            'first_name', 'last_name'))
        return HttpResponse(json_data, content_type='application/json')
