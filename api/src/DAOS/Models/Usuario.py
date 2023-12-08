import datetime

from src.db import db

class Usuario(db.Model):
	idusuario = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(45), unique=False, nullable=False)
	apellido = db.Column(db.String(45), unique=False, nullable=False)
	usuario = db.Column(db.String(45), unique=False, nullable=False)
	contrasena = db.Column(db.String(45), unique=False, nullable=False)
	timestamp = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	valid = db.Column(db.Integer, unique=False, nullable=False)

	tareas = db.relationship('Tarea', backref='Usuario', lazy=True)

	def __init__(self, idusuario, nombre, apellido, usuario, contrasena, valid, tareas):
		self.idusuario = idusuario
		self.nombre = nombre
		self.apellido = apellido
		self.usuario = usuario
		self.contrasena = contrasena
		self.valid = valid
		self.tareas = tareas
