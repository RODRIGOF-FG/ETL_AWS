# ETL_AWS

Proceso ETL (Extract, Transform, Load), el cual implica la carga de un archivo CSV en un bucket de Amazon S3 , mediante el servicio Glue de AWS, se lleva a cabo la transformación para posteriormente cargarlo o consultar su contenido a través de una base de datos en Amazon Athena.


### Paso 1

**IAM – Roles**

- Para crear un rol, debemos dirigirnos al panel del servicio Identity and Access Management (IAM) e ingresar a la opción de "Roles".

![img_1](file/img_1.png)

- Presionamos la opción de "Crear Rol" y luego seleccionamos "Servicio de AWS". Además, en el apartado de "Servicios de caso de uso", agregamos el servicio "Glue" y presionamos el botón siguiente.

![img_2](file/img_2.png) ![img_3](file/img_3.png)

- En el apartado de "Agregar permisos", otorgamos el permiso de "Amazon S3 Full Access" y continuamos.

![img_4](file/img_4.png)

- En el apartado de "Asignar nombre, revisar y crear", asignamos un nombre al rol que estamos creando, en este caso, "aws_rol", y hacemos clic en "Crear".

![img_5](file/img_5.png)

- Para verificar si el rol creado se ha guardado correctamente, puedes dirigirte a la sección de "Roles".

![img_6](file/img_6.png)

### Paso 2

**Crear Bucket**

- Para crear un bucket nos dirigimos al servicio de Amazon S3 de AWS y luego vamos a la opción de *"Buckets"*.

![img_7](file/img_7.png)

- Presionamos en "Crear Bucket", y luego debemos asignar un nombre único al bucket, en este caso, "bucket-aws-1", y procedemos a crearlo.

![img_8](file/img_8.png)

- Después, nos dirigimos al bucket creado para crear carpetas que se utilizarán en este ejemplo.
Creamos 4 carpetas llamadas: "csv_input" (donde colocaremos el archivo CSV que vamos a transformar), "csv_output" (donde se guardará el archivo de salida después de la transformación en el servicio Glue), "script", y "temp".

![img_9](file/img_9.png)

- Carpeta de "csv_input", con el CSV que utilizaremos:

![img_10](file/img_10.png)



### Paso 3

**AWS Glue**

- Ingresamos al servicio "AWS Glue" y accedemos a la opción de "ETL visual" para crear un job.















