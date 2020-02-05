from ...app import ma
from marshmallow import Schema
from ..Models.Usuario import Usuario

#Forma manual

class UsuarioSchema(ma.Schema):
	class Meta:
		# Fields to expose
		fields = ("idusuario","nombre","apellido","usuario","timestamp","valid")

"""
#Todo el modelo completo
class UsuarioSchema(ma.ModelSchema):
	class Meta:
		model = Usuario
"""