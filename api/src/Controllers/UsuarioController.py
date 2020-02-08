from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from ..app import app;

from ..Services.UsuarioService import UsuarioService
from ..Services.VOS.UsuarioVO import UsuarioVO

usuarioBluePrint = Blueprint('usuario', 'usuario', url_prefix='/usuario')

@usuarioBluePrint.route('', methods=['POST'])
def guardar():
	print('UsuarioController guardar()')
	nombre = request.form.get("nombre")
	apellido = request.form.get("apellido")
	usuario = request.form.get("usuario")
	contrasena = request.form.get("contrasena")
	enviar = True
	mensajes = "Te falta"
	if(nombre==None):
		enviar = False
		mensajes +="Nombre"
	if(apellido==None):
		enviar = False
		mensajes +="Apellido"
	if(usuario==None):
		enviar = False
		mensajes +="Usuario"
	if(contrasena==None):
		enviar = False
		mensajes +="Contrasena"

	if(enviar):
		usuarioVO = UsuarioVO()
		usuarioVO.nombre = nombre
		usuarioVO.apellido = apellido
		usuarioVO.usuario = usuario
		usuarioVO.contrasena = contrasena
		respuesta = UsuarioService.guardar(usuarioVO)
	else:
		respuesta = {"result":False, "errores":mensajes}

	return jsonify(respuesta)

@usuarioBluePrint.route('/<int:idusuario>', methods=['PUT'])
def editar(idusuario):
	print('UsuarioController editar()')
	nombre = request.form.get("nombre")
	apellido = request.form.get("apellido")
	usuario = request.form.get("usuario")
	contrasena = request.form.get("contrasena")
	valid = request.form.get("valid")
	enviar = True
	mensajes = "Te falto"
	if(nombre==None):
		enviar = False
		mensajes +="Nombre"
	if(apellido==None):
		enviar = False
		mensajes +="Apellido"
	if(usuario==None):
		enviar = False
		mensajes +="Usuario"
	if(contrasena==None):
		enviar = False
		mensajes +="Contrasena"
	if(valid==None):
		enviar = False
		mensajes +="Valid"

	if(enviar):
		usuarioVO = UsuarioVO()
		usuarioVO.idusuario = idusuario
		usuarioVO.nombre = nombre
		usuarioVO.apellido = apellido
		usuarioVO.usuario = usuario
		usuarioVO.contrasena = contrasena
		usuarioVO.valid = valid
		respuesta = UsuarioService.editar(usuarioVO)
	else:
		respuesta = {"result":False, "errores":mensajes}
	return jsonify(respuesta)

@usuarioBluePrint.route('/<int:idusuario>', methods=['DELETE'])
def eliminar(idusuario):
	print('UsuarioController eliminar()')
	respuesta = UsuarioService.eliminar(idusuario)
	return jsonify(respuesta)

@usuarioBluePrint.route('/pagina/<int:pagina>', methods=['GET'])
def obtener(pagina):
	print('UsuarioController obtener()')
	respuesta = UsuarioService.obtener(pagina)
	return jsonify(respuesta)

@usuarioBluePrint.route('/<int:idusuario>', methods=['GET'])
def obtenerConID(idusuario):
	print('UsuarioController obtenerConID()')
	respuesta = UsuarioService.obtenerConID(idusuario)
	return jsonify(respuesta)

app.register_blueprint(usuarioBluePrint)