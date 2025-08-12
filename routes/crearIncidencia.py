from flask import Blueprint, jsonify, request
from pymongo import MongoClient
from marshmallow import ValidationError
import os
from schemas.validarIncidencias import validarIncidenciaSchema
#Creamos una instancia de blueprint para poder utilizar nuestra ruta como backend.
crearIncidencia_bp = Blueprint('crearincidencia_bp', __name__)

#Creamos las credenciales de nuestra conexión a la db
client = MongoClient(os.getenv("MONGO_URI"))
#Nos conectamos a nuestra base de datos
db = client["pruebas_mido"]
#Usamos la colección de datos llamada incidencias.
coleccion_incidencias = db["incidencias"]
#Creamos una ruta blueprint para registrar las incidencias usando los métodos de POST y OPTIONS
@crearIncidencia_bp.route('/registrarIncidencia', methods=["POST", "OPTIONS"])
#Creamos una función la cuál será la encargada de registrar la incidencia dentro de nuestra base de datos.
def registrarIncidencia():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'message':str(e)}),500