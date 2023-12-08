from flask import request
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from src.app import app

from src.Services.UsuarioService import UsuarioService

usuarioBluePrint = Blueprint('usuario', 'usuario', url_prefix='/usuario')

class UsuarioController():

	@usuarioBluePrint.route('', methods=['POST'])
	def guardar():
		print(colored("UsuarioController: guardar() {}".format(request.form), 'green'))
		return UsuarioService.guardar(request)

	@usuarioBluePrint.route('/', methods=['GET'])
	def obtener():
		print('UsuarioController: obtener()')
		respuesta = UsuarioService.obtener()
		return jsonify(respuesta)

	@usuarioBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
	def obtenerPaginado(pagina):
		print('UsuarioController: obtenerPaginado() de pagina {}'.format(pagina))
		respuesta = UsuarioService.obtenerPaginado(pagina)
		return jsonify(respuesta)

	@usuarioBluePrint.route('/<int:idUsuario>', methods=['GET'])
	def obtenerConID(idUsuario):
		print(colored("UsuarioController: obtenerConID() {}".format(idUsuario), 'green'))
		return UsuarioService.obtenerConID(idUsuario)

	@usuarioBluePrint.route('/<int:idUsuario>', methods=['PUT'])
	def editar(idUsuario):
		print(colored("UsuarioController: editar() {}".format(request.form), 'green'))
		return UsuarioService.editar(request)
		
	@usuarioBluePrint.route('/<int:idUsuario>', methods=['DELETE'])
	def eliminar(idUsuario):
		print(colored("UsuarioController: eliminar() {}".format(idUsuario), 'green'))
		return UsuarioService.eliminar(idUsuario)

app.register_blueprint(usuarioBluePrint)