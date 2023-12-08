from ...app import ma
from marshmallow import Schema, fields
from ..Models.Usuario import Usuario
from .TareaSchema import TareaSchema

#Forma manual
'''
class UsuarioSchema(ma.Schema):
	class Meta:
		# Fields to expose
		#fields = ("idusuario","nombre","apellido","usuario","timestamp","valid")
'''
#Todo el modelo completo
class UsuarioSchema(ma.ModelSchema):
	class Meta:
		model = Usuario
		ordered = True

	idusuario = fields.Integer()
	nombre = fields.String()
	apellido = fields.String()
	usuario = fields.String()
	timestamp = fields.DateTime()
	valid = fields.Integer()
	tareas = fields.List(fields.Nested(TareaSchema))
