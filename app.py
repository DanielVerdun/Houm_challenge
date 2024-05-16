from datetime import datetime
from flask import Flask, jsonify, request   # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_marshmallow import Marshmallow # type: ignore
from flask_migrate import Migrate # type: ignore
from marshmallow import fields # type: ignore


# ============================ Configuración BBDD =================================
# Para configurar una base de datos en Flask, necesitarás seguir algunos pasos básicos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)


# Modelo de Empleado:
class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    correo_electronico = db.Column(db.String(100), unique=True, nullable=False)

    def __init__(self, nombre, correo_electronico):
        self.nombre = nombre
        self.correo_electronico = correo_electronico

class EmpleadoSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombre', 'correo_electronico')

# Crea una instancia del esquema de Empleado
empleado_schema = EmpleadoSchema()
empleados_schema = EmpleadoSchema(many=True)



# Modelo de Propiedad:
class Propiedad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direccion = db.Column(db.String(200), nullable=False)
    ubicacion = db.Column(db.String(100))
    precio = db.Column(db.Float)
    descripcion = db.Column(db.Text)

    def __init__(self, direccion, ubicacion,precio,descripcion):
        self.direccion = direccion
        self.ubicacion = ubicacion
        self.precio = precio
        self.descripcion = descripcion

class PropiedadSchema(ma.Schema):
    class Meta:
        fields = ('id', 'direccion', 'ubicacion','precio','descripcion')

propiedad_schema = PropiedadSchema()
propiedades_schema = PropiedadSchema(many=True)



# Modelo de Visita a la Propiedad:
class Visita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    propiedad_id = db.Column(db.Integer, db.ForeignKey('propiedad.id'), nullable=False)
    fecha_hora_visita = db.Column(db.DateTime, nullable=False, default=datetime.now)  # Aquí se establece el valor predeterminado a la fecha y hora actuales
    comentario = db.Column(db.Text)

    empleado = db.relationship('Empleado', backref='visitas')
    propiedad = db.relationship('Propiedad', backref='visitas')

    def __init__(self, empleado_id, propiedad_id,comentario):
        self.empleado_id = empleado_id
        self.propiedad_id = propiedad_id
        #self.fecha_hora_visita = fecha_hora_visita
        self.comentario = comentario

class VisitaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'empleado_id', 'propiedad_id','fecha_hora_visita','comentario')

visita_schema = VisitaSchema()
visitas_schema = VisitaSchema(many=True)


# db.ForeignKey() se utiliza para establecer las relaciones entre las entidades.
# db.relationship() se utiliza para definir la relación entre las tablas y acceder a los datos relacionados.





# =========================== Endpoint API - EMPLEADOS ============================

@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

# Metodo POST para crear un nuevo empleado
# http://127.0.0.1:5000/empleados
@app.route('/empleados', methods=['Post'])
def crear_empleado():
    #id = request.json['id']
    nombre = request.json['nombre']
    correo_electronico = request.json['correo_electronico']

    nuevo_empleado = Empleado(nombre=nombre, correo_electronico=correo_electronico)
    db.session.add(nuevo_empleado)
    db.session.commit()

    return empleado_schema.jsonify(nuevo_empleado)

# Metodo GET - Obtener todos los empleados
# http://127.0.0.1:5000/empleados
@app.route('/empleados', methods=['GET'])
def get_empleados():
    empleados = Empleado.query.all()
    result = empleados_schema.dump(empleados)

    return jsonify(result)

# Metodo GET - Obtener un empleado pasando un id por parámetro
# http://127.0.0.1:5000/empleados/<id>
@app.route('/empleados/<id>', methods=['GET'])
def get_empleado(id):
    buscar_empleado = Empleado.query.get(id)

    return empleado_schema.jsonify(buscar_empleado)

# Metodo PUT - Actualizar un empleado pasando un id por parámetro
# http://127.0.0.1:5000/empleados/<id>
@app.route('/empleados/<id>', methods=['PUT'])
def update_empleado(id):
    empleado = Empleado.query.get(id)

    nombre = request.json['nombre']
    correo_electronico = request.json['correo_electronico']

    empleado.nombre = nombre
    empleado.correo_electronico = correo_electronico

    db.session.commit()

    return empleado_schema.jsonify(empleado)

# Metodo DELETE - Eliminar un empleado pasando un id por parámetro
# http://127.0.0.1:5000/empleados/<id>
@app.route('/empleados/<id>', methods=['DELETE'])
def delete_empleado(id):
    empleado = Empleado.query.get(id)
    db.session.delete(empleado)
    db.session.commit()

    return empleado_schema.jsonify(empleado)

# =========================== Fin Endpoint API - EMPLEADOS ============================





# =========================== Endpoint API - PROPIEDADES ===============================

# Metodo POST para crear una propiedad
# http://127.0.0.1:5000/propiedades
@app.route('/propiedades', methods=['Post'])
def crear_propiedad():
    #id = request.json['id']
    direccion = request.json['direccion']
    ubicacion = request.json['ubicacion']
    precio = request.json['precio']
    descripcion = request.json['descripcion']

    nuevo_propiedad = Propiedad(direccion=direccion, ubicacion=ubicacion,precio=precio, descripcion=descripcion)
    db.session.add(nuevo_propiedad)
    db.session.commit()

    return propiedad_schema.jsonify(nuevo_propiedad)

# Metodo GET - Obtener todas las propiedades
# http://127.0.0.1:5000/propiedades
@app.route('/propiedades', methods=['GET'])
def get_propiedades():
    propiedades = Propiedad.query.all()
    result = propiedades_schema.dump(propiedades)

    return jsonify(result)

# Metodo GET - Obtener una propiedad pasando un id por parámetro
# http://127.0.0.1:5000/propiedades/<id>
@app.route('/propiedades/<id>', methods=['GET'])
def get_propiedad(id):
    buscar_propiedad = Propiedad.query.get(id)

    return propiedad_schema.jsonify(buscar_propiedad)

# Metodo PUT - Actualizar una propiedad pasando un id por parámetro
# http://127.0.0.1:5000/propiedades/<id>
@app.route('/propiedades/<id>', methods=['PUT'])
def update_propiedad(id):
    propiedad = Propiedad.query.get(id)

    direccion = request.json['direccion']
    ubicacion = request.json['ubicacion']
    precio = request.json['precio']
    descripcion = request.json['descripcion']

    propiedad.direccion = direccion
    propiedad.ubicacion = ubicacion
    propiedad.precio = precio
    propiedad.descripcion = descripcion

    db.session.commit()

    return propiedad_schema.jsonify(propiedad)

# Metodo DELETE - Eliminar una propiedad pasando un id por parámetro
# http://127.0.0.1:5000/propiedades/<id>
@app.route('/propiedades/<id>', methods=['DELETE'])
def delete_propiedad(id):
    propiedad = Propiedad.query.get(id)
    db.session.delete(propiedad)
    db.session.commit()

    return propiedad_schema.jsonify(propiedad)

# =========================== Fin Endpoint API - PROPIEDADES ============================





# =========================== Endpoint API - VISITAS ===============================

# Metodo POST para crear una visia
# http://127.0.0.1:5000/visitas
@app.route('/visitas', methods=['Post'])
def crear_visita():
    #id = request.json['id']
    empleado_id = request.json['empleado_id']
    propiedad_id = request.json['propiedad_id']
    #fecha_hora_visita = request.json['fecha_hora_visita']
    comentario = request.json['comentario']

    nueva_visita = Visita(empleado_id=empleado_id, propiedad_id=propiedad_id, comentario=comentario)
    db.session.add(nueva_visita)
    db.session.commit()

    return visita_schema.jsonify(nueva_visita)

# Metodo GET - Obtener todas las visitas
# http://127.0.0.1:5000/visitas
@app.route('/visitas', methods=['GET'])
def get_visitas():
    visitas = Visita.query.all()
    result = visitas_schema.dump(visitas)

    return jsonify(result)

# Metodo GET - Obtener una visita pasando un id por parámetro
# http://127.0.0.1:5000/visitas/<id>
@app.route('/visitas/<id>', methods=['GET'])
def get_visita(id):
    buscar_visita = Visita.query.get(id)

    return visita_schema.jsonify(buscar_visita)

# Metodo PUT - Actualizar una visita pasando un id por parámetro
# http://127.0.0.1:5000/visitas/<id>
@app.route('/visitas/<id>', methods=['PUT'])
def update_visita(id):
    visita = Visita.query.get(id)

    dempleado_id = request.json['empleado_id']
    propiedad_id = request.json['propiedad_id']
    fecha_hora_visita = request.json['fecha_hora_visita']
    comentario = request.json['comentario']

    visita.direccion = dempleado_id
    visita.ubicacion = propiedad_id
    visita.precio = fecha_hora_visita
    visita.descripcion = comentario

    db.session.commit()

    return visita_schema.jsonify(visita)

# Metodo DELETE - Eliminar una visita pasando un id por parámetro
# http://127.0.0.1:5000/visitas/<id>
@app.route('/visitas/<id>', methods=['DELETE'])
def delete_visita(id):
    visita = Visita.query.get(id)
    db.session.delete(visita)
    db.session.commit()

    return visita_schema.jsonify(visita)



if __name__ == '__main__':
    app.run(debug=True)