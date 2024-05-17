## Medo de ejecución local
Crear un directorio local
    
    mkdir test_repo

Ingresar al directorio:

    cd test_repo

Crear un etorno virtual:

    python3 -m venv env

Activar entorno:

    source env/bin/activate

Clonar repositorio:




Este código define un conjunto de endpoints de una API para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la entidad "Empleado". Aquí está la documentación para cada endpoint:

## Empleados
Crear un nuevo empleado:

    Método: POST
    Ruta: /empleados
    Parámetros JSON requeridos:
        nombre (str): Nombre del empleado.
        correo_electronico (str): Correo electrónico del empleado.
    Descripción: Crea un nuevo empleado con el nombre y correo electrónico proporcionados en el cuerpo de la solicitud.
    Respuesta exitosa:
    Retorna los datos del nuevo empleado en formato JSON.
    Ejemplo de uso: POST http://127.0.0.1:5000/empleados
   
    {
      "nombre":"empleado1",
      "correo_electronico":"empleado1@gmail.com"
    }

Obtener todos los empleados:

    Método: GET
    Ruta: /empleados
    Descripción: Obtiene todos los empleados almacenados en la base de datos.
    Respuesta exitosa:
    Retorna una lista de todos los empleados en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/empleados


Obtener un empleado por ID:

    Método: GET
    Ruta: /empleados/<id>
    Parámetros de ruta:
        id (int): ID del empleado que se desea obtener.
    Descripción: Obtiene un empleado específico mediante su ID.
    Respuesta exitosa:
    Retorna los datos del empleado solicitado en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/empleados/1
    
Actualizar un empleado:

    Método: PUT
    Ruta: /empleados/<id>
    Parámetros de ruta:
        id (int): ID del empleado que se desea actualizar.
    Parámetros JSON requeridos:
        nombre (str): Nuevo nombre del empleado.
        correo_electronico (str): Nuevo correo electrónico del empleado.
    Descripción: Actualiza los datos de un empleado existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos del empleado actualizado en formato JSON.
    Ejemplo de uso: PUT http://127.0.0.1:5000/empleados/1
    
    {
      "nombre":"Carlos",
      "correo_electronico":"empleado1@gmail.com"
    }
    
Eliminar un empleado:

    Método: DELETE
    Ruta: /empleados/<id>
    Parámetros de ruta:
        id (int): ID del empleado que se desea eliminar.
    Descripción: Elimina un empleado existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos del empleado eliminado en formato JSON.
    Ejemplo de uso: DELETE http://127.0.0.1:5000/empleados/1


## Propiedades
Crear una nueva propiedad:
    
    Método: POST
    Ruta: /propiedades
    Parámetros JSON requeridos:
        direccion (str): Direccion de la propiedad.
        ubicacion (str): Ciudad donde se encuentra.
        precio (float): Valor en dolares
        descripcion (str): Descripcion o comentarios de la propiedad
    Descripción: Crea una nueva propiedad con la direccion, ubicacion, precio, y descripción proporcionados en el cuerpo de la solicitud.
    Respuesta exitosa:
    Retorna los datos de la nueva propiedad en formato JSON.
    Ejemplo de uso: POST http://127.0.0.1:5000/propiedades
   
    {
      "direccion":"calle_1234",
      "ubicacion":"Barrio Norte",
      "precio":40.000,
      "descripcion":"Descripción de la casa 1"
    }
Obtener todos las propiedades:

    Método: GET
    Ruta: /propiedades
    Descripción: Obtiene todos las propiedades almacenados en la base de datos.
    Respuesta exitosa:
    Retorna una lista de todos las propiedades en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/propiedades


Obtener una propiedad por ID:

    Método: GET
    Ruta: /propiedades/<id>
    Parámetros de ruta:
        id (int): ID de la propiedad que se desea obtener.
    Descripción: Obtiene una propiedad específica mediante su ID.
    Respuesta exitosa:
    Retorna los datos de la propiedad solicitada en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/propiedades/1
    
Actualizar una propiedad:

    Método: PUT
    Ruta: /propiedades/<id>
    Parámetros de ruta:
        id (int): ID del empleado que se desea actualizar.
    Parámetros JSON requeridos:
        direccion (str): Direccion de la propiedad.
        ubicacion (str): Ciudad donde se encuentra.
        precio (float): Valor en dolares
        descripcion (str): Descripcion o comentarios de la propiedad
    Descripción: Actualiza los datos de una propiedades existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos de la propiedades actualizado en formato JSON.
    Ejemplo de uso: PUT http://127.0.0.1:5000/propiedades/2
    
    {
      "direccion":"calle_4556",
      "ubicacion":"Barrio Solares",
      "precio":110.000,
      "descripcion":"Descripción de la casa 2"
    }
        
Eliminar una propiedad:

    Método: DELETE
    Ruta: /propiedades/<id>
    Parámetros de ruta:
        id (int): ID de la propiedad que se desea eliminar.
    Descripción: Elimina una propiedades existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos del empleado eliminado en formato JSON.
    Ejemplo de uso: DELETE http://127.0.0.1:5000/propiedades/1

## Vsitas
Crear una nueva visita:
    
    Método: POST
    Ruta: /visitas
    Parámetros JSON requeridos:
        empleado_id (str): Id del empleado.
        propiedad_id (str): Id de la propiedad.
        comentario (str): Descripcion o comentarios de la visitas
    Descripción: Crea una nueva visitas con  empleado_id, propiedad_id, comentario,proporcionados en el cuerpo de la solicitud.
    Respuesta exitosa:
    Retorna los datos de la nueva visitas en formato JSON.
    Ejemplo de uso: POST http://127.0.0.1:5000/visitas
   
   {
      "empleado_id":70,
      "propiedad_id":1,
      "comentario":"Comentario_3"
    }

Obtener todos las visitas:

    Método: GET
    Ruta: /visitas
    Descripción: Obtiene todos las visitas almacenados en la base de datos.
    Respuesta exitosa:
    Retorna una lista de todos las visitas en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/visitas


Obtener una visita por ID:

    Método: GET
    Ruta: /visitas/<id>
    Parámetros de ruta:
        id (int): ID de la visitas que se desea obtener.
    Descripción: Obtiene una visitas específica mediante su ID.
    Respuesta exitosa:
    Retorna los datos de la visitas solicitada en formato JSON.
    Ejemplo de uso: GET http://127.0.0.1:5000/visitas/1
    
Actualizar una visita:

    Método: PUT
    Ruta: /visitas/<id>
    Parámetros de ruta:
        id (int): ID del visitas que se desea actualizar.
    Parámetros JSON requeridos:
        empleado_id (str): Id del empleado.
        propiedad_id (str): Id de la propiedad.
        comentario (str): Descripcion o comentarios de la visitas
    Descripción: Actualiza los datos de una visita existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos de la visita actualizado en formato JSON.
    Ejemplo de uso: PUT http://127.0.0.1:5000/visitas/2
    
    {
      "empleado_id":70,
      "propiedad_id":3,
      "comentario":"Comentario_3"
    }

Eliminar una visita:

    Método: DELETE
    Ruta: /visitas/<id>
    Parámetros de ruta:
        id (int): ID de la visita que se desea eliminar.
    Descripción: Elimina una visita existente mediante su ID.
    Respuesta exitosa:
    Retorna los datos de la visita eliminada en formato JSON.
    Ejemplo de uso: DELETE http://127.0.0.1:5000/visitas/1

