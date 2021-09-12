# S.U. Logistics

Hecho con python 3.7, el entorno virtual se encuentra en la carpeta *venv*.  
En caso contrario se debe instalar los requerimientos:
```
pip install -r requirements.txt
```

# URL Donde se encuentra desplegada la aplicación:
```
```
# Documentación
### ¿Cómo ejecutar localmente?
Para inicar Django use el siguiente comando en la carpeta LogisticsApp:  
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Ingrese a la dirección proporcionada para dicho fin (e.g. http://127.0.0.1:8000/)  
Este aplicativo usa una base de datos mysql alojada en: **https://console.clever-cloud.com/**  
  
Para el modelamiento de la base de datos se hizo uso de Enterprise Architect, en la carpeta DB se encuentra:  
- Modelo relacional (Tenga en cuenta que no se encuentran en dicho modelo los campos requeridos por Django para usuarios como *is_active*, entre otros)
- Script que contiene la visualización de la base de datos (Debe conectarse usando la respectiva configuración que se presenta acontinuación usando MySQL Workbench):
```
        'NAME': 'bunmran84krjxio4vd1m'
        'USER': 'uv1dexbw5zehhogt'
        'PASSWORD': 'A1wD9OZmhD9gDIH1kveP'
        'HOST': 'bunmran84krjxio4vd1m-mysql.services.clever-cloud.com'
        'PORT': '3306'
```
Si desea conectarse manualmente a la base de datos para realizar querys en ella por medio de la consola de MySQL por favor use el siguiente comando:
```
mysql -h bunmran84krjxio4vd1m-mysql.services.clever-cloud.com -P 3306 -u uv1dexbw5zehhogt -p bunmran84krjxio4vd1m
```

**EN CASO DE QUERER USAR UNA BASE DE DATOS LOCAL**:
- Configure dicha base de datos en *MainApp/settings.py*
- Ejecute los siguientes comandos:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
- Para crear los registros en la base de datos ingrese a http://127.0.0.1:8000/registrar , dicha pantalla cargará los registros a la base de datos y posteriormente redireccionará a el login, puede tardar un poco, por favor espere, en la
consola donde se ejecuta Django puede observar como se cargan los registros.  
*Nota*: Los registros son cargados a partir del archivo *DB/DB_Datos.csv*, este archivo fue generado por medio de el script *modify_BD.R* que se encuentra también en dicha carpeta, el cual cambia:  
- Formato de las fechas a YYYY-MM-DD de las columnas *f_nacimiento* y *f_ingreso*.  
- Elimina el primer "." y el signo "$" de todos los registros en la columna *v_ventas2019*
- Elimina todos los "." de la columna *k_cedula*  
- Elimina los guiones de la columna *o_telefono*
- Elimina las comillas dobles de las columnas *v_ventas2019*, *o_telefono* y *k_cedula*
- Reemplaza todos NA de la columna *v_ventas2019* con 0.000  