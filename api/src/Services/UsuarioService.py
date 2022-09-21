from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored

from ..app import db

from ..DAOS.Models.Usuario import Usuario
from ..DAOS.Schemas.UsuarioSchema import UsuarioSchema
from ..DAOS.UsuarioDAO import UsuarioDAO

from .VOS.UsuarioVO import UsuarioVO

class UsuarioService():

	def __init__(self):
		print('UsuarioService')

	@staticmethod
	def guardar(request):
		print(colored("UsuarioService: guardar(); {}".format(request.form), 'cyan'))
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
			respuesta = UsuarioDAO.guardar(usuarioVO)
			print(colored(respuesta, 'cyan'))
			if(respuesta["result"]):
				usuario = UsuarioSchema().dump(respuesta["usuario"])
				respuesta["usuario"] = usuario
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener(pagina):
		respuesta = UsuarioDAO.obtener(pagina)
		if(respuesta["result"]):
			respuesta["usuarios"] = UsuarioSchema(many=True).dump(respuesta["usuarios"])

	@staticmethod
	def obtenerConID(idUsuario):
		print(colored("UsuarioService: obtenerConID(); {}".format(idUsuario), 'cyan'))
		usuario = UsuarioDAO.obtenerConID(idUsuario)
		if(usuario is not None):
			return {
				"result": True,
				"usuario": UsuarioSchema().dump(usuario),
				"mensajes": "Se encontró usuario con id {}".format(idUsuario)
			}
		else:
			return {
				"result": False,
				"mensajes": "No se encontró usuario con id {}".format(idUsuario)
			}

	@staticmethod
	def editar(request):
		print(colored("UsuarioService: editar(); {}".format(request.form), 'cyan'))
		idUsuario = request.form.get("idUsuario")
		nombre = request.form.get("nombre")
		apellido = request.form.get("apellido")
		usuario = request.form.get("usuario")
		contrasena = request.form.get("contrasena")
		valid = request.form.get("valid")
		enviar = True
		mensajes = "Te faltó:"
		if(idUsuario==None):
			enviar = False
			mensajes +="\nid del usuario"
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
			respuesta = UsuarioDAO.editar(usuarioVO)
			print(colored(respuesta, 'cyan'))
			if(respuesta["result"]):
				usuario = UsuarioSchema().dump(respuesta["usuario"])
				respuesta["usuario"] = usuario
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(idUsuario):
		print(colored("UsuarioService: eliminar(); {}".format(idUsuario), 'cyan'))
		respuesta = UsuarioDAO.eliminar(idUsuario)
		return respuesta
