from ..app import db

from termcolor import colored

from ..DAOS.Models.Usuario import Usuario
from ..DAOS.Schemas.UsuarioSchema import UsuarioSchema
from ..DAOS.UsuarioDAO import UsuarioDAO

from .VOS.UsuarioVO import UsuarioVO

class UsuarioService():

	def __init__(self):
		print('UsuarioService')

	@staticmethod
	def guardar(usuarioVO):
		print(colored("UsuarioService: guardar(); {}".format(usuarioVO.usuario), 'cyan'))
		respuesta = UsuarioDAO.guardar(usuarioVO)
		print(colored(respuesta, 'cyan'))

		if(respuesta["result"]):
			usuario = UsuarioSchema().dump(respuesta["usuario"])
			respuesta["usuario"] = usuario
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
	def editar(usuarioVO):
		print(colored("UsuarioService: editar(); {}".format(usuarioVO.idusuario), 'cyan'))
		respuesta = UsuarioDAO.editar(usuarioVO)
		print(colored(respuesta, 'cyan'))
		if(respuesta["result"]):
			usuario = UsuarioSchema().dump(respuesta["usuario"])
			respuesta["usuario"] = usuario
		return respuesta

	@staticmethod
	def eliminar(idUsuario):
		print(colored("UsuarioService: eliminar(); {}".format(idUsuario), 'cyan'))
		respuesta = UsuarioDAO.eliminar(idUsuario)
		return respuesta
