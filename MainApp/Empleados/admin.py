from django.contrib import admin
from django.contrib.auth import get_user_model

# Obtiene el modelo del empleado
Empleado = get_user_model()

# Registra el modelo Empleado en el sitio administrativo
admin.site.register(Empleado)
