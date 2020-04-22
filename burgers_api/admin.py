from django.contrib import admin
from .models import Hamburguesa, Ingredientes

# Register your models here.

admin.site.register(Hamburguesa)
admin.site.register(Ingredientes)