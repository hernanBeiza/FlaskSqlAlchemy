
"""
from flask import Flask
from flask import Blueprint

from app import app;
"""

print("routes iniciar();")

from .Controllers.UsuarioController import *
from .Controllers.IndexController import *

"""
indexBluePrint = Blueprint('index', 'index', url_prefix='/')
@indexBluePrint.route('/', methods=['GET'])
def home():
	return 'Bienvenido a mi primera API con Python y Flask'

usuarioBluePrint = Blueprint('usuario', 'usuario', url_prefix='/usuario')
@usuarioBluePrint.route('/', methods=['GET'])
def home():
	return 'Bienvenido a usuario'

app.register_blueprint(indexBluePrint)
app.register_blueprint(usuarioBluePrint)
"""

"""
@app.route('/', methods=['GET'])
def home():
	return 'Bienvenido a mi primera API con Python y Flask'

@app.route('/usuario', methods=['GET', 'POST'])
def usuario():
  return 'Soy post de usuario'

@app.route('/saludar/<nombre>', methods=['GET'])
def saudar(nombre):
  # show the user profile for that user
  return 'Hola %s' % escape(nombre)

@app.route('/obtener/<int:id>', methods=['GET'])
def show_post(id):
  # show the post with the given id, the id is an integer
	mensajes = 'Obteniendo con id %s' % id
	return jsonify(result=True, mensajes=mensajes)
"""