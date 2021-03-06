"""MainApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

'''
Manejo de todas las URLs asociadas al aplicativo web, incluye todas las URLs de todas las aplicaciones
'''

# URLs asociadas al proyecto
urlpatterns = [
    path('', include('Empleados.urls'), name='Empleado'),  # Manejo de empleados
    path('admin/', admin.site.urls),  # URLs administrativas
]
