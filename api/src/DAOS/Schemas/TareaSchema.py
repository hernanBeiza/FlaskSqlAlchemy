from ...app import ma
from marshmallow import Schema, fields
from ..Models.Tarea import Tarea

#TODO Deprecado
#Forma manual
"""
class TareaSchema(ma.Schema):
	class Meta:
		# Fields to expose
		fields = ("idtarea","idusuario","titulo","timestamp","valid")
		ordered = True
"""

#Todo el modelo completo
class TareaSchema(ma.ModelSchema):
	class Meta:
		model = Tarea
		ordered = True

	idtarea = fields.Integer(data_key="id")
	idusuario = fields.Integer(data_key="idUsuario")
	titulo = fields.String()
	timestamp = fields.DateTime()
	valid = fields.Integer()
