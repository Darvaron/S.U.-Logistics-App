from django.shortcuts import get_object_or_404, render, redirect,HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .utils import *
import csv

'''
Manejo de la base de datos para Empleado, contiene las funciones y clases necesarios para interactuar con dicha base y
generar las vistas correspondientes
'''
# Obtiene el modelo del Empleado
Empleado = get_user_model()

# Guarda los rangos para mapear y comparar entre jefe y empleado y determinar si tiene acceso al dicho perfil
Rango = {"Ejecutivo Comercial": 0, "Subgerente Regional": 1, "Gerente Regional": 2,
         "Gerente Comercial": 4, "Asistente de Gerencia": 3}


def ProfileView(request, o_numero):
    '''
    Genera la vista correspondiente al perfil del empleado de número o_numero
    :param request: REQUEST
    :param o_numero: Número del perfil deseado este es el número del empleado en la empresa
    :return: Renderiza la página correspondiente
    '''

    global Rango  # Solicita los rangos globales

    if not request.user.is_authenticated:  # Si no ha iniciado sesión
        print("No ha iniciado sesión")
        return LoginView(request)
    # Si ya inició sesión
    print("Entra al perfil: {}".format(o_numero))

    ventas_totales = obtenerVentas(o_numero)  # Obtiene las ventas totales asociadas al empleado de número o_numero
    empleadoActual = Empleado.objects.get(o_numero=o_numero)  # Obtiene el empleado de número o_numero
    jefe = obtenerJefe(o_numero)  # Obtiene el jefe de dicho empleado, None en caso de no tener

    esSuperior = False  # Bandera que determina si el perfil del jefe es superior al actual
    autorizado = True  # Evita que entre a un URL de un perfil de mayor rango modificando la URL

    if jefe != None and Rango[jefe.o_cargo] > Rango[request.user.o_cargo]:  # Si el jefe no es superior y tiene jefe
        esSuperior = True  # Autorización para link hacia el jefe
    if Rango[empleadoActual.o_cargo] > Rango[request.user.o_cargo]:
        '''
        Verifica que pueda acceder a dicho perfil, asi evita acceder a perfil de sus superiores modificando la URL en el
        buscador, solo permite que acceda a perfiles de rango menor.
        '''
        autorizado = False  # No puede entrar al perfil actual por ser de menor rango que el requerido

    # Obtiene sus subalternos
    subalternos = [[s.n_nombres, s.n_apellido1, s.n_apellido2, s.o_numero, obtenerVentas(s.o_numero)] for s in
                   Empleado.objects.filter(
                       o_jefe=o_numero)]  # Lista por comprensión que guarda nombre completo, número y
    # ventas totales de sus subalternos directos
    # Redirección al perfil
    return render(request, "empleados/perfil.html", {"empleado": empleadoActual,
                                                     "ventas": ventas_totales, 'superior': esSuperior, 'jefe': jefe,
                                                     "subalternos": subalternos, "autorizado": autorizado})


def LogoutView(request):
    '''
    Cierra sesión
    :param request: REQUEST
    :return: Redirección al login
    '''
    logout(request)
    messages.info(request, "Sesión cerrada satisfactoriamente")
    return LoginView(request)


def LoginView(request):  # Encargado de la dirección /, corresponde a la página principal del aplicativo
    '''
    Al ingresar a la dirección / comprueba si el usuario ya inicio sesión en cuyo caso le muestra su perfil
    En caso de no haber iniciado sesión lo redirecciona al login
    :param request: Request
    :return: Redirección a login si no ha iniciado sesión, si ya lo ha hecho lo redirecciona a su perfil
    '''

    if not request.user.is_authenticated:  # Si no ha iniciado sesión
        if request.method == "POST":  # Si ya ingreso sus datos
            form = AuthenticationForm(request, data=request.POST)

            if form.is_valid():  # Si el formulario es válido
                email = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(o_email=email, password=password)

                if user is not None:  # Si el email y contraseña son válidos
                    login(request, user)
                    messages.info(request, f"Ingresando como {email}")
                    return ProfileView(request, request.user.o_numero)  # Redirección a su perfil
        # Si no ingresado al login
        form = AuthenticationForm()
        return render(request=request, template_name="empleados/login.html",
                      context={"login_form": form})  # Redirección al login
    else:  # Si ya inicio sesión
        print("Ingresando al perfil de {}".format(request.user.o_numero))
        return ProfileView(request, request.user.o_numero)


def RegistroEmpleadoV(request):
    '''
    Al ingresar a la dirección /registrar/ genera el registro en la base de datos de todos los empleados y posteriormente
    redirige al login, esta función es usada para ingresar todos los empleados automaticamente a la base de datos si esta
    se esta CREANDO POR PRIMERA VEZ
    ESTE PROCESO PUEDE TARDAR DEBIDO A LA VELOCIDAD DE LA BASE DE DATOS AL SER UNA VERSIÓN GRATUITA CON MEMORIA COMPARTIDA
    :param request: REQUEST
    :return: redirección a la página del login después de ingresar los empleados en la base de datos
    '''

    # Obtiene el modelo de la App
    Empleado = get_user_model()

    # Lectura de registros del csv
    file = '../DB/BD_Datos.csv'
    data = csv.reader(open(file), delimiter=",")

    print('Por favor espere mientras se ingresan los registros a la base de datos...')

    counter = 0
    # FALTA RENDERIZAR ACÁ LA PÁGINA DE ESPERA

    for row in data:  # Ingresa cada uno de los registros dentro de la base de datos

        if counter == 0:  # Ignora la cabezera del .csv
            counter += 1
        else:
            print("Ingresando al usuario de cédula: {}".format(row[3]))
            # Separa los valores del csv
            n_nombres = row[0]
            n_apellido1 = row[1]
            n_apellido2 = row[2]
            k_cedula = row[3]
            f_nacimiento = row[4]
            i_genero = row[5]
            f_ingreso = row[6]
            o_numero = row[7]
            o_cargo = row[8]
            o_jefe = row[9]
            o_zona = row[10]
            n_municipio = row[11]
            n_departamento = row[12]
            v_ventas2019 = row[13]
            o_email = row[14]
            password = row[15]
            o_imagen = row[16]
            o_telefono = row[17]

            # Crea un registro Empleado para ser ingresado en la base de datos
            empleado = Empleado(
                o_email=o_email,
                n_nombres=n_nombres, n_apellido1=n_apellido1, n_apellido2=n_apellido2, k_cedula=k_cedula,
                f_nacimiento=f_nacimiento, i_genero=i_genero, f_ingreso=f_ingreso, o_numero=o_numero, o_cargo=o_cargo,
                o_jefe=o_jefe, o_zona=o_zona, n_municipio=n_municipio, n_departamento=n_departamento,
                v_ventas2019=v_ventas2019, o_imagen=o_imagen, o_telefono=o_telefono
            )

            empleado.set_password(password)
            # Guarda el registro en la base de datos
            empleado.save()

    # Al finalizar la creación de los registros redirecciona al login
    return redirect('../')
