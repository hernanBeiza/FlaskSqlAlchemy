class UsuarioVO():

	idusuario = None
	nombre = None
	apellido = None
	usuario = None
	contrasena = None
	valid = None

	#def __init__(self):

	@staticmethod
	def withUsuario(usuario):
		if(usuario is not None):
			vo = UsuarioVO()
			vo.idusuario = usuario.idusuario
			vo.nombre = usuario.nombre
			vo.apellido = usuario.apellido
			vo.usuario = usuario.usuario
			vo.contrasena = usuario.contrasena
			vo.valid = usuario.valid
			return vo
		return None