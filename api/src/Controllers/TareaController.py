from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from ..app import app;

from ..Services.TareaService import TareaService
from ..Services.VOS.TareaVO import TareaVO

tareaBluePrint = Blueprint('tarea', 'tarea', url_prefix='/tarea')

class TareaController():

	@tareaBluePrint.route('', methods=['POST'])
	def guardar():
		print(colored("TareaController: guardar()", 'green'))
		return TareaService.guardar(request)

	@tareaBluePrint.route('/', methods=['GET'])
	def obtener():
		print(colored("TareaController: obtener()", 'green'))
		return TareaService.obtener()

	@tareaBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
	def obtenerConPagina(pagina):
		print(colored("TareaController: obtenerConPagina() {}".format(pagina), 'green'))
		respuesta = TareaService.obtenerConPagina(pagina)
		return jsonify(respuesta)

	@tareaBluePrint.route('/<int:idTarea>', methods=['GET'])
	def obtenerConID(idTarea):
		print(colored("TareaController: obtenerConID() {}".format(idTarea), 'green'))
		return TareaService.obtenerConID(idTarea)

	@tareaBluePrint.route('/usuario/<int:idUsuario>', methods=['GET'])
	def obtenerConIDUsuario(idUsuario):
		print(colored("TareaController: obtenerConIDUsuario() {}".format(idUsuario), 'green'))
		return TareaService.obtenerConIDUsuario(idUsuario)

	@tareaBluePrint.route('/<int:idTarea>', methods=['PUT'])
	def editar(idTarea):
		return TareaService.editar(request)

	@tareaBluePrint.route('/<int:idTarea>', methods=['DELETE'])
	def eliminar(idTarea):
		print(colored("TareaController: eliminar() {}".format(idTarea), 'green'))
		return TareaService.eliminar(idTarea)

app.register_blueprint(tareaBluePrint)