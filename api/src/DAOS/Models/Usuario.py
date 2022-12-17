import datetime

from src.DB import DB

class Usuario(DB.obtener().Model):
	idusuario = DB.obtener().Column(DB.obtener().Integer, primary_key=True)
	nombre = DB.obtener().Column(DB.obtener().String(45), unique=False, nullable=False)
	apellido = DB.obtener().Column(DB.obtener().String(45), unique=False, nullable=False)
	usuario = DB.obtener().Column(DB.obtener().String(45), unique=False, nullable=False)
	contrasena = DB.obtener().Column(DB.obtener().String(45), unique=False, nullable=False)
	timestamp = DB.obtener().Column(DB.obtener().DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	valid = DB.obtener().Column(DB.obtener().Integer, unique=False, nullable=False)

	tareas = DB.obtener().relationship('Tarea', backref='Usuario', lazy=True)

	def __init__(self, idusuario, nombre, apellido, usuario, contrasena, valid, tareas):
		self.idusuario = idusuario
		self.nombre = nombre
		self.apellido = apellido
		self.usuario = usuario
		self.contrasena = contrasena
		self.valid = valid
		self.tareas = tareas
