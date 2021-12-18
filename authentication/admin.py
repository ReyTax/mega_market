from django.contrib import admin
from authentication.models import Client
# Register your models here.


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
