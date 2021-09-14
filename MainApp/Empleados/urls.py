from django.urls import path
from .views import RegistroEmpleadoV, LoginView, ProfileView, LogoutView

'''
Manejo de las URLs asociadas a Empleado
'''

# Nombre de la aplicación para identificación de URLs
app_name = "Empleado"

# URLs asociadas
urlpatterns = [
    path("registrar/", RegistroEmpleadoV, name="registrarEmpleados"), # Carga de registros cuando se crea la base de datos
    path('', LoginView, name="login"), # Página principal
    path('perfil/<int:o_numero>/', ProfileView, name="perfil"), # Perfil correspondiente al empleado de número o_numero
    path('logout/', LogoutView, name="logout") # Cerrar sesión
]
