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
		print(colored("UsuarioController: guardar()", 'green'))
		nombre = request.form.get("nombre")
		apellido = request.form.get("apellido")
		usuario = request.form.get("usuario")
		contrasena = request.form.get("contrasena")
		enviar = True
		mensajes = "Te falta:"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(apellido==None):
			enviar = False
			mensajes +="\nApellido"
		if(usuario==None):
			enviar = False
			mensajes +="\nUsuario"
		if(contrasena==None):
			enviar = False
			mensajes +="\nContrasena"

		if(enviar):
			usuarioVO = UsuarioVO()
			usuarioVO.nombre = nombre
			usuarioVO.apellido = apellido
			usuarioVO.usuario = usuario
			usuarioVO.contrasena = contrasena
			respuesta = UsuarioService.guardar(usuarioVO)
		else:
			respuesta = {"result":False, "errores":mensajes}

		return respuesta

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
		print(colored("UsuarioController: editar() {}".format(idUsuario), 'green'))
		nombre = request.form.get("nombre")
		apellido = request.form.get("apellido")
		usuario = request.form.get("usuario")
		contrasena = request.form.get("contrasena")
		valid = request.form.get("valid")
		enviar = True
		mensajes = "Te faltó:"
		if(nombre==None):
			enviar = False
			mensajes +="\nNombre"
		if(apellido==None):
			enviar = False
			mensajes +="\nApellido"
		if(usuario==None):
			enviar = False
			mensajes +="\nUsuario"
		if(contrasena==None):
			enviar = False
			mensajes +="\nContrasena"
		if(valid==None):
			enviar = False
			mensajes +="\nValid"

		if(enviar):
			usuarioVO = UsuarioVO()
			usuarioVO.idusuario = idUsuario
			usuarioVO.nombre = nombre
			usuarioVO.apellido = apellido
			usuarioVO.usuario = usuario
			usuarioVO.contrasena = contrasena
			usuarioVO.valid = valid
			respuesta = UsuarioService.editar(usuarioVO)
		else:
			respuesta = {"result":False, "errores":mensajes}
		return jsonify(respuesta)

	@usuarioBluePrint.route('/<int:idUsuario>', methods=['DELETE'])
	def eliminar(idUsuario):
		print(colored("UsuarioController: eliminar() {}".format(idUsuario), 'green'))
		return UsuarioService.eliminar(idUsuario)

app.register_blueprint(usuarioBluePrint)