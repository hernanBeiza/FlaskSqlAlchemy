import datetime

from src.db import db

class Tarea(db.Model):
	idtarea = db.Column(db.Integer, primary_key=True)
	titulo = db.Column(db.String(45), unique=False, nullable=False)
	timestamp = db.Column(db.DateTime(), unique=False, nullable=False, default=datetime.datetime.utcnow)
	valid = db.Column(db.Integer, unique=False, nullable=False)

	idusuario = db.Column(db.Integer, db.ForeignKey('usuario.idusuario'), nullable=False)

	def __init__(self, idtarea, titulo, valid, idusuario):
		self.idtarea = idtarea
		self.titulo = titulo
		self.valid = valid
		self.idusuario = idusuario
