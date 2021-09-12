from django.urls import path
from .views import RegistroEmpleadoV

'''
Manejo de las URLs asociadas a Empleado
'''

# Nombre de la aplicación para identificación de URLs
app_name = "Empleado"

# URLs asociadas
urlpatterns = [
    path("registrar/", RegistroEmpleadoV, name="registrarEmpleados")
]
