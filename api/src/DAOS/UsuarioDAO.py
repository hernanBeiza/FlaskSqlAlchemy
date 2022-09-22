from termcolor import colored

from ..app import db

from ..DAOS.Models.Usuario import Usuario

class UsuarioDAO():

	'''
	def __init__(self):
		print('UsuarioDAO')
	'''

	@staticmethod
	def guardar(usuarioVO):
		print(colored("UsuarioService: guardar(); {}".format(usuarioVO.usuario), 'yellow'))
		usuario = Usuario(None, usuarioVO.nombre, usuarioVO.apellido, usuarioVO.usuario, usuarioVO.contrasena, 2, [])
		db.session.add(usuario)
		result=True
		mensajes="Usuario guardado correctamente"
		try:
			db.session.commit()
			print(colored("UsuarioService: usuario guardado correctamente", 'yellow'))
			#usuario = Usuario.query.get(usuario.idusuario)
		except Exception as e:
			print (e)
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			db.session.rollback()
			# for resetting non-commited .add()
			db.session.flush()
			result=False
			mensajes="El usuario no se pudo guardar"
		respuesta = {"result":result,"mensajes":mensajes, "usuario":usuario}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("UsuarioService: obtener();", 'yellow'))
		return Usuario.query.all()

	@staticmethod
	def obtenerConID(idUsuario):
		print(colored("UsuarioService: obtenerConID(); {}".format(idUsuario), 'yellow'))
		return Usuario.query.get(idUsuario)

	@staticmethod
	def editar(usuarioVO):
		print(colored("UsuarioService: editar(); {}".format(usuarioVO.idusuario), 'yellow'))
		result=True
		mensajes="Usuario editado correctamente"
		try:
			usuario = Usuario.query.get(usuarioVO.idusuario)
			usuario.nombre = usuarioVO.nombre;
			usuario.apellido = usuarioVO.apellido;
			usuario.usuario = usuarioVO.usuario;
			usuario.contrasena = usuarioVO.contrasena;
			usuario.valid = usuarioVO.valid;
			db.session.commit()
			#usuario = Usuario.query.get(usuario.idusuario)
		except Exception as e:
			print (e)
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			db.session.rollback()
			# for resetting non-commited .add()
			db.session.flush()
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
				db.session.delete(usuario)
				db.session.commit()
				respuesta = {"result":result,"mensajes":mensajes}
				return respuesta
			except Exception as e:
				print ("Error al eliminar el usuario con id {}. Error: {}".format(idUsuario, e))
				#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
				db.session.rollback()
				# for resetting non-commited .add()
				db.session.flush()
				result=False
				mensajes="El usuario con id {} no se pudo eliminar".format(idUsuario)
		else:
			result=False
			mensajes="El usuario con id {} no se ha podido encontrar".format(idUsuario)

		respuesta = {"result":result,"errores":mensajes}
		return respuesta
