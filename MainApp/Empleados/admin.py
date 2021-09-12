from django.contrib import admin
from django.contrib.auth import get_user_model

# Obtiene el modelo del empleado
Empleado = get_user_model()

# Registra al empleado en la base de datos
admin.site.register(Empleado)
