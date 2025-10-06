from django.contrib import admin

# Register your models here.

from .models import Clientes
# registrar el modelo Clientes en el admin
admin.site.register(Clientes)