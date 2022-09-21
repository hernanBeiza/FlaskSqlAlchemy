from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from ..app import app;

from ..Services.UsuarioService import UsuarioService
from ..Services.VOS.UsuarioVO import UsuarioVO

usuarioBluePrint = Blueprint('usuario', 'usuario', url_prefix='/usuario')

class UsuarioController():

	@usuarioBluePrint.route('', methods=['POST'])
	def guardar():
		print(colored("UsuarioController: guardar() {}".format(request.form), 'green'))
		return UsuarioService.guardar(request)

	@usuarioBluePrint.route('/', methods=['GET'])
	def obtener(pagina):
		print('UsuarioController: obtener()')
		respuesta = UsuarioService.obtener(pagina)
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