from marshmallow import Schema, fields
from termcolor import colored

from ...app import ma
from ...DAOS.Models.Usuario import Usuario
from ..VOS.UsuarioVO import UsuarioVO
from ...DAOS.Schemas.UsuarioSchema import UsuarioSchema
from .TareaVOBuilder import TareaVOBuilder


class UsuarioVOBuilder(Schema):
	class Meta:
			model = Usuario
			ordered = True

	idusuario = fields.Integer(data_key="id")
	nombre = fields.String()
	apellido = fields.String()
	usuario = fields.String()
	timestamp = fields.DateTime()
	valid = fields.Integer()
	tareas = fields.List(fields.Nested(TareaVOBuilder))

	usuario = None
	usuarios = None

	#def __init__(self):

	@staticmethod
	def fromUsuario(usuario):
		UsuarioVOBuilder.usuario = usuario
		return UsuarioVOBuilder()

	@staticmethod
	def build():		
		if(UsuarioVOBuilder().usuario is None):
			print("No se puede contruir UsuarioVO. usuario is None")
			return None
		else:
			try:
				return UsuarioVOBuilder().dump(UsuarioVOBuilder.usuario)
			except Exception as e: 
				print(colored("No se puede contruir UsuarioVO. Error en UsuarioVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def fromUsuarios(usuarios):
		UsuarioVOBuilder.usuarios = usuarios
		return UsuarioVOBuilder()

	@staticmethod
	def builds():		
		if(UsuarioVOBuilder().usuarios is None):
			print("No se puede contruir UsuarioVO. usuarios is None")
			return None
		else:
			try:
				return UsuarioVOBuilder(many=True).dump(UsuarioVOBuilder.usuarios)
			except Exception as e: 
				print(colored("No se puede contruir UsuarioVO. Error en UsuarioVOBuilder; {}".format(e), 'red'))
