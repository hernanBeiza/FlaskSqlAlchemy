from ...app import db
class Usuario(db.Model):
	idusuario = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(45), unique=False, nullable=False)
	apellido = db.Column(db.String(45), unique=False, nullable=False)
	usuario = db.Column(db.String(45), unique=False, nullable=False)
	contrasena = db.Column(db.String(45), unique=False, nullable=False)
	timestamp = db.Column(db.DateTime(), unique=False, nullable=False)
	valid = db.Column(db.Integer, unique=False, nullable=False)

	def __init__(self, idusuario, nombre, apellido, usuario, contrasena, valid):
		self.idusuario = idusuario
		self.nombre = nombre
		self.apellido = apellido
		self.usuario = usuario
		self.contrasena = contrasena
		self.valid = valid

	@classmethod
	def withUsuarioVO(self, usuarioVO):
		if(usuarioVO is not None):
			usuario = Usuario(usuarioVO.idusuario,usuarioVO.nombre,usuarioVO.apellido,usuarioVO.usuario,usuarioVO.contrasena,usuarioVO.valid)
			return usuario
		return None