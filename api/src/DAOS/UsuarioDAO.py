from termcolor import colored

from src.DB import DB

from src.DAOS.Models.Usuario import Usuario

class UsuarioDAO():

	'''
	def __init__(self):
		print('UsuarioDAO')
	'''

	@staticmethod
	def guardar(usuarioVO):
		print(colored("UsuarioDAO: guardar(); {}".format(usuarioVO.usuario), 'yellow'))
		usuario = Usuario(None, usuarioVO.nombre, usuarioVO.apellido, usuarioVO.usuario, usuarioVO.contrasena, 2, [])
		try:
			DB.obtener().session.add(usuario)
			DB.obtener().session.commit()
			print(colored("UsuarioDAO: usuario guardado correctamente", 'yellow'))
			result=True
			mensajes="Usuario guardado correctamente"
			#usuario = Usuario.query.get(usuario.idusuario)
		except Exception as e:
			print(colored("UsuarioDAO: Usuario no se pudo guardar", 'red'))
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			DB.obtener().session.rollback()
			# for resetting non-commited .add()
			DB.obtener().session.flush()
			result=False
			mensajes="El usuario no se pudo guardar"
		respuesta = {"result":result,"mensajes":mensajes, "usuario":usuario}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("UsuarioDAO: obtener();", 'yellow'))
		return Usuario.query.all()

	@staticmethod
	def obtenerConID(idUsuario):
		print(colored("UsuarioDAO: obtenerConID(); {}".format(idUsuario), 'yellow'))
		return Usuario.query.get(idUsuario)

	@staticmethod
	def editar(usuarioVO):
		print(colored("UsuarioDAO: editar(); {}".format(usuarioVO.idusuario), 'yellow'))
		result=True
		mensajes="Usuario editado correctamente"
		try:
			usuario = Usuario.query.get(usuarioVO.idusuario)
			usuario.nombre = usuarioVO.nombre;
			usuario.apellido = usuarioVO.apellido;
			usuario.usuario = usuarioVO.usuario;
			usuario.contrasena = usuarioVO.contrasena;
			usuario.valid = usuarioVO.valid;
			DB().obtener().session.commit()
			#usuario = Usuario.query.get(usuario.idusuario)
		except Exception as e:
			print ("Usuario con id {} no se pudo editar. {}".format(usuarioVO.id,e))
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			DB.obtener().session.rollback()
			# for resetting non-commited .add()
			DB.obtener().session.flush()
			result=False
			mensajes="El usuario no se pudo editar"
		respuesta = {"result":result,"mensajes":mensajes, "usuario":usuario}
		return respuesta

	@staticmethod
	def eliminar(idUsuario):
		result = True
		mensajes = "Usuario con id {} eliminado correctamente".format(idUsuario)
		usuario = Usuario.query.get(idUsuario)
		if(usuario is not None):
			try:
				DB.obtener().session.delete(usuario)
				DB.obtener().session.commit()
				respuesta = {"result":result,"mensajes":mensajes}
				return respuesta
			except Exception as e:
				print ("Error al eliminar el usuario con id {}. Error: {}".format(idUsuario, e))
				#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
				DB.obtener().session.rollback()
				# for resetting non-commited .add()
				DB.obtener().session.flush()
				result=False
				mensajes="El usuario con id {} no se pudo eliminar".format(idUsuario)
		else:
			result=False
			mensajes="El usuario con id {} no se ha podido encontrar".format(idUsuario)

		respuesta = {"result":result,"errores":mensajes}
		return respuesta
