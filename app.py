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
empleado = EmpleadoSchema()
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
    fecha_hora_visita = db.Column(db.DateTime, nullable=False)
    comentario = db.Column(db.Text)

    empleado = db.relationship('Empleado', backref='visitas')
    propiedad = db.relationship('Propiedad', backref='visitas')

    def __init__(self, empleado_id, propiedad_id,fecha_hora_visita,comentario):
        self.empleado_id = empleado_id
        self.propiedad_id = propiedad_id
        self.fecha_hora_visita = fecha_hora_visita
        self.comentario = comentario

class VisitaSchema(ma.Schema):
    class Meta:
        fields = ('id', 'empleado_id', 'propiedad_id','fecha_hora_visita','comentario')

visita_schema = VisitaSchema()
visitas_schema = VisitaSchema(many=True)


# db.ForeignKey() se utiliza para establecer las relaciones entre las entidades.
# db.relationship() se utiliza para definir la relación entre las tablas y acceder a los datos relacionados.


# =========================== Endpoint de la API ============================

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

    return empleado.jsonify(nuevo_empleado)



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
    return empleado.jsonify(buscar_empleado)




if __name__ == '__main__':
    app.run(debug=True)