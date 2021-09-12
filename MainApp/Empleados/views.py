from django.shortcuts import render
from django.contrib.auth import login, get_user_model
import csv

'''
Manejo de la base de datos para Empleado, contiene las funciones y clases necesarios para interactuar con dicha base
'''


def RegistroEmpleadoV(request):
    '''
    Al ingresar a la página /registrar/ genera el registro en la base de datos de todos los empleados y posteriormente
    redirige al login, esta función es usado para ingresar todos los empleados automaticamente a la base de datos si esta
    se esta creando por primera vez
    :param request: REQUEST
    :return: redirección a la página del login después de ingresar los usuarios en la base de datos
    '''

    # Obtiene el modelo de la App
    Empleado = get_user_model()

    # Lectura de registros del csv
    file = '../DB/BD_Datos.csv'
    data = csv.reader(open(file), delimiter=",")

    print('Por favor espere mientras se ingresan los registros a la base de datos...')

    counter = 0
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
    return render(request=request, template_name="empleados/login.html")
