from marshmallow import Schema, fields
from termcolor import colored

from ...app import ma
from ...DAOS.Models.Tarea import Tarea
from ..VOS.TareaVO import TareaVO
from ...DAOS.Schemas.TareaSchema import TareaSchema

class TareaVOBuilder(ma.ModelSchema):
	class Meta:
		model = Tarea
		ordered = True

	#Schema
	##Modelo - Dato a mostrar
	idtarea = fields.Integer(data_key="id")
	idusuario = fields.Integer(data_key="idUsuario")
	titulo = fields.String()
	timestamp = fields.DateTime()
	valid = fields.Integer()


	tarea = None
	tareas = None

	#def __init__(self):

	@staticmethod
	def fromTarea(tarea):
		TareaVOBuilder.tarea = tarea
		return TareaVOBuilder()

	@staticmethod
	def fromTareas(tareas):
		TareaVOBuilder.tareas = tareas
		return TareaVOBuilder()

	@staticmethod
	def build():
		if(TareaVOBuilder.tarea is None):
			print("No se puede contruir TareaVO. tareas is None")
			return None
		else:
			try:
				return TareaVOBuilder().dump(TareaVOBuilder.tarea)
			except Exception as e:
				print(colored("No se puede contruir TareaVO. Error en TareaVOBuilder; {}".format(e), 'red'))

	@staticmethod
	def builds():
		if(TareaVOBuilder.tareas is None):
			print("No se puede contruir TareaVO. tareas is None")
			return None
		else:
			try:
				return TareaVOBuilder(many=True).dump(TareaVOBuilder.tareas)
			except Exception as e:
				print(colored("No se puede contruir TareaVO. Error en TareaVOBuilder; {}".format(e), 'red'))
