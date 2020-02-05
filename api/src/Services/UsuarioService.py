from ..app import db

from ..DAOS.Models.Usuario import Usuario
from ..DAOS.Schemas.UsuarioSchema import UsuarioSchema

from ..DAOS.UsuarioDAO import UsuarioDAO
from termcolor import colored

from .VOS.UsuarioVO import UsuarioVO

class UsuarioService():

	def __init__(self):
		print('UsuarioService')

	@staticmethod
	def guardar(usuarioVO):
		respuesta = UsuarioDAO.guardar(usuarioVO)
		print(colored(respuesta, 'green'))

		if(respuesta["result"]):
			usuarioSchema = UsuarioSchema()
			usuario = usuarioSchema.dump(respuesta["usuario"])
			respuesta["usuario"] = usuario
		return respuesta

	@staticmethod
	def editar(usuarioVO):
		respuesta = UsuarioDAO.editar(usuarioVO)
		print(colored(respuesta, 'green'))

		if(respuesta["result"]):
			usuarioSchema = UsuarioSchema()
			usuario = usuarioSchema.dump(respuesta["usuario"])
			respuesta["usuario"] = usuario
		return respuesta

	@staticmethod
	def eliminar(idusuario):
		respuesta = UsuarioDAO.eliminar(idusuario)
		print(colored(respuesta, 'green'))
		return respuesta

	@staticmethod
	def obtener(pagina):
		respuesta = UsuarioDAO.obtener(pagina)
		if(respuesta["result"]):
			usuariosSchema = UsuarioSchema(many=True)
			respuesta["usuarios"] = usuariosSchema.dump(respuesta["usuarios"])

	@staticmethod
	def obtenerConID(idusuario):
		respuesta = UsuarioDAO.obtenerConID(idusuario)
		if(respuesta["result"]):
			usuarioSchema = UsuarioSchema()
			respuesta["usuario"] = usuarioSchema.dump(respuesta["usuario"])

		return respuesta