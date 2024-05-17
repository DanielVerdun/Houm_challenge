
from app import app, db
#from flask import Flask # type: ignore
#from flask_sqlalchemy import SQLAlchemy # type: ignore
import unittest
from app import Empleado, Propiedad, Visita # type: ignore


class TestModels(unittest.TestCase):

    def setUp(self):

        #self.app = Flask(__name__)  # Si tienes una función create_app() para crear tu aplicación Flask
        #self.app_context = self.app.app_context()
        #self.app_context.push()

        # Configurar el contexto de la aplicación
        #self.app = app.test_client()
        #db.create_all()

        # Crear un cliente de prueba
        self.app = app.test_client()

        # Configurar el contexto de la aplicación
        #self.app_context = self.app.app_context()
        #self.app_context.push()

        # Crear las tablas en la base de datos
        #db.create_all()

    def tearDown(self):
        #self.app = app.test_client()

        #db.session.remove()
        #db.drop_all()
        #self.app_context.pop()

        # Limpiar la base de datos y cerrar la sesión
        #db.session.remove()
        #db.drop_all()
        pass


    def test_visita_model(self):
        empleado = Empleado(nombre="Nombre", correo_electronico="correo@example.com")
        db.session.add(empleado)
        db.session.commit()

        propiedad = Propiedad(direccion="Dirección", ubicacion="Ubicación", precio=1000.0, descripcion="Descripción")
        db.session.add(propiedad)
        db.session.commit()

        visita = Visita(empleado_id=empleado.id, propiedad_id=propiedad.id, comentario="Comentario")
        db.session.add(visita)
        db.session.commit()

        self.assertIsNotNone(visita.id)



if __name__ == '__main__':
    unittest.main()
