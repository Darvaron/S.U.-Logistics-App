from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

'''
Funciones utiles para calculos relacionados con el empleado
'''

Empleado = get_user_model()


def obtenerJefe(o_numero):
    '''
    Retorna el jefe del empleado de número o_numero
    :param o_numero: Número del empleado en la empresa
    :return: Objeto Empleado correspondiente al jefe
    '''
    empleadoActual = Empleado.objects.get(o_numero=o_numero)
    jefe = None
    try:  # Intenta obtener el jefe del empleado de número o_numero
        jefe = Empleado.objects.get(o_numero=empleadoActual.o_jefe)
    except ObjectDoesNotExist as ne:  # Si no tiene jefe
        print("No tiene jefe")
    return jefe


def obtenerVentas(o_numero):
    '''
    De manera recursiva calcula el valor de las ventas asociadas al empleado de número o_numero
    :param o_numero: Número del empleado en la empresa
    :return: Valor de las ventas asociadas a dicho empleado
    '''
    empleadoActual = Empleado.objects.get(o_numero=o_numero)  # Empleado actual
    # Si no es ejecutivo comercial
    if empleadoActual.o_cargo != "Ejecutivo Comercial":
        ventasEmpleados = 0
        queryEmpleados = Empleado.objects.filter(o_jefe=o_numero)  # Subalternos

        '''
        Calcula las ventas totales de sus subalternos por medio de un mapping recursivo
        '''
        queryEmpleados = [e.o_numero for e in queryEmpleados]
        ventasEmpleados = sum(map(obtenerVentas, queryEmpleados))
        '''
        Forma iterativa 
        for empleado in queryEmpleados:
            ventasEmpleados += obtenerVentas(empleado.o_numero)  # Invocación recursiva
        '''

        return ventasEmpleados

    else:  # Si es ejecutivo comercial
        return empleadoActual.v_ventas2019
