from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

'''
CONTIENE:
- EmpleadoManager: Manejador del empleado
- Empleado: Contiene el modelo de empleado
'''

class EmpleadoManager(BaseUserManager):
    '''
    Clase correspondiente al manejador del empleado, extiende del manejador de usuario por defecto de Django
    '''
    def create_user(self, n_nombres, n_apellido1, n_apellido2, k_cedula, f_nacimiento,
                    i_genero, f_ingreso, o_numero, o_cargo, o_jefe, o_zona, n_municipio,
                    n_departamento, v_ventas2019, o_email, password, o_imagen, o_telefono):
        '''
        Genera un nuevo registro de Empleado en la base de datos a partir de los datos proporcionados
        :return: Nuevo empleado
        '''
        empleado = self.model(
            o_email=self.normalize_email(o_email),
            n_nombres=n_nombres, n_apellido1=n_apellido1, n_apellido2=n_apellido2, k_cedula=k_cedula,
            f_nacimiento=f_nacimiento, i_genero=i_genero, f_ingreso=f_ingreso, o_numero=o_numero,
            o_cargo=o_cargo, o_jefe=o_jefe, o_zona=o_zona, n_municipio=n_municipio, n_departamento=n_departamento,
            v_ventas2019=v_ventas2019, o_imagen=o_imagen, o_telefono=o_telefono
        )

        empleado.set_password(password)
        empleado.save(using=self._db)

        return empleado


class Empleado(AbstractBaseUser):
    '''
    Descripción: Contiene el modelo de Empleado, hereda de la clase de usuario, con el fin de obtener seguridad,
    fiabilidad y control de acceso al aplicativo web
    Dicho modelo se encuentra en el archivo de Data Modelling de la carpeta DB
    Se definen los siguientes prefijos para el modelo:
    n: nombres
    k: primary key
    f: fecha
    i: identificador (categoria)
    o: otro
    v: número con decimal
    Contiene los siguientes atributos:
    - n_nombres: Nombres del empleado
    - n_apellido1: Primer apellido del empleado
    - n_apellido2: Segundo apellido del empleado
    - k_cedula: Cédula del empleado - primary key de la tabla, debe ser mayor a 0
    - f_nacimiento: Fecha de nacimiento del empleado
    - i_genero: Identificador del genero del empleado, 'M' o 'F'
    - f_ingreso: Fecha de ingreso del empleado
    - o_numero: Número de identificación del empleado
    - o_cargo: Cargo del empleado
    - o_jefe: Número de identificación del jefe del empleado.
    - o_zona: Zona del empleado.
    - n_municipio: Nombre del municipio donde reside el empleado.
    - n_departamento: Nombre del departamento donde reside el empleado
    - v_ventas2019: Valor de las ventas correspondientes a dicho empleado. (Depende del tipo de cargo)
    - o_email: Email del empleado.
    - o_imagen: Ruta a la imagen de perfil del empleado.
    - o_telefono: Número de teléfono del empleado.

    NO es necesario agregar un campo para la contraseña ya que esta es incluida por defecto en el modelo

    Poseen las siguientes configuraciones:
    max_length -- Longitud máxima de VARCHAR
    primary_key -- Primary key de la tabla
    max_digits -- Dígitos después de la coma
    decimal_places -- Posiciones decimales
    '''

    n_nombres = models.EmailField(max_length=40)
    n_apellido1 = models.CharField(max_length=20)
    n_apellido2 = models.CharField(max_length=20)
    k_cedula = models.DecimalField(primary_key=True, max_digits=10, decimal_places=0)
    f_nacimiento = models.DateField()
    i_genero = models.CharField(max_length=1)
    f_ingreso = models.DateField()
    o_numero = models.IntegerField(default=0)
    o_cargo = models.CharField(max_length=50)
    o_jefe = models.IntegerField(null=True, default=0)
    o_zona = models.CharField(max_length=30)
    n_municipio = models.CharField(max_length=30)
    n_departamento = models.CharField(max_length=30)
    v_ventas2019 = models.DecimalField(max_digits=10, decimal_places=3, default=0.000)
    o_email = models.EmailField(unique=True, max_length=40)
    o_imagen = models.CharField(max_length=20)
    o_telefono = models.DecimalField(max_digits=10, decimal_places=0)

    # Atributos requeridos por la clase AbstractBaseUser

    is_active = models.BooleanField(default=True)  # Se encuentra activo el empleado?
    staff = models.BooleanField(default=False)  # Es parte del staff del sitio web?
    admin = models.BooleanField(default=False)  # Es admin del sitio web?

    '''
    No es necesario agregar un campo para la clave ya que este se incluye por defecto
    '''

    # Correspondiente al método de logueo
    USERNAME_FIELD = 'o_email'

    # Campos requeridos al crear un usuario
    REQUIRED_FIELDS = [n_nombres, n_apellido1, n_apellido2, k_cedula, f_nacimiento,
                       i_genero, f_ingreso, o_numero, o_cargo, o_jefe, o_zona, n_municipio,
                       n_departamento, v_ventas2019, o_imagen, o_telefono]

    def get_email(self): # Retorna el email del usuario
        return self.o_email

    def __str__(self): # Retorna el email del usuario por medio de __str__
        return self.o_email

    def has_perm(self, perm, obj=None):
        '''¿Tiene permisos especificos?'''
        return True

    def has_module_perms(self, app_label):
        '''¿Tiene permisos para ver el modulo app_label?'''
        return False

    # Decoradores requeridos por parte de la clase AbstractBaseUser

    @property
    def is_staff(self):
        '''¿Es parte del staff del aplicativo?'''
        return self.staff

    @property
    def is_admin(self):
        '''¿Es administrador?'''
        return self.admin

    # Manejador del empleado
    objects = EmpleadoManager()

    class Meta:
        # db_table -- Nombre de la tabla correspondiente en la base de datos
        db_table = 'Empleado'