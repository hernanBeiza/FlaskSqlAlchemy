import datetime

from src.DB import DB

class Tarea(DB.obtener().Model):
	idtarea = DB.obtener().Column(DB.obtener().Integer, primary_key=True)
	titulo = DB.obtener().Column(DB.obtener().String(45), unique=False, nullable=False)
	timestamp = DB.obtener().Column(DB.obtener().DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	valid = DB.obtener().Column(DB.obtener().Integer, unique=False, nullable=False)

	idusuario = DB.obtener().Column(DB.obtener().Integer, DB.obtener().ForeignKey('usuario.idusuario'), nullable=False)

	def __init__(self, idtarea, titulo, valid, idusuario):
		self.idtarea = idtarea
		self.titulo = titulo
		self.valid = valid
		self.idusuario = idusuario
