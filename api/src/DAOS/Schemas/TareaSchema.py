from src.ma import ma
from marshmallow import Schema, fields
from src.DAOS.Models.Tarea import Tarea

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

	idtarea = fields.Integer()
	idusuario = fields.Integer()
	titulo = fields.String()
	timestamp = fields.DateTime()
	valid = fields.Integer()
