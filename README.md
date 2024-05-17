Este código define un conjunto de endpoints de una API para manejar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre la entidad "Empleado". Aquí está la documentación para cada endpoint:

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
    Obtener todos los empleados:

Listar empleados:

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
Eliminar un empleado:

Método: DELETE
Ruta: /empleados/<id>
Parámetros de ruta:
    id (int): ID del empleado que se desea eliminar.
Descripción: Elimina un empleado existente mediante su ID.
Respuesta exitosa:
Retorna los datos del empleado eliminado en formato JSON.
Ejemplo de uso: DELETE http://127.0.0.1:5000/empleados/1
