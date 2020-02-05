from termcolor import colored

from ..app import db

from ..DAOS.Models.Usuario import Usuario
from ..DAOS.Schemas.UsuarioSchema import UsuarioSchema

class UsuarioDAO():

	def __init__(self):
		print('UsuarioDAO')

	@staticmethod
	def guardar(usuarioVO):
		usuario = Usuario(None,usuarioVO.nombre, usuarioVO.apellido, usuarioVO.usuario, usuarioVO.contrasena, 2)
		db.session.add(usuario)
		result=True
		mensajes="Usuario guardado correctamente"
		try:
			db.session.commit()
			usuario = Usuario.query.get(usuario.idusuario)
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
	def editar(usuarioVO):
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
	def eliminar(idusuario):
		result=True
		mensajes="Usuario eliminado correctamente"
		usuario = Usuario.query.get(idusuario)
		if(usuario is not None):
			try:
					db.session.delete(usuario)
					db.session.commit()
			except Exception as e:
				print (e)
				#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
				db.session.rollback()
				# for resetting non-commited .add()
				db.session.flush()
				result=False
				mensajes="El usuario no se pudo eliminar"
		else:
			result=False
			mensajes="El usuario no se ha podido encontrar"

		respuesta = {"result":result,"mensajes":mensajes}
		return respuesta

	@staticmethod
	def obtener(pagina):
		result = True
		mensajes = "Usuarios encontrados correctamente"
		totalPorPagina = 2
		usuariosEncontrados = Usuario.query.paginate(pagina,int(totalPorPagina), False).items

		if(len(usuariosEncontrados)==0):
			result=False
			mensajes="No se han encontrado usuarios"

		respuesta = {"result":result,"mensajes":mensajes, "usuarios":usuariosEncontrados}
		return respuesta

	@staticmethod
	def obtenerConID(idusuario):
		result = True
		mensajes = "Usuarios encontrados correctamente"
		usuarioEncontrado = Usuario.query.get(idusuario)
		if(usuarioEncontrado is None):
			result = False
			mensajes = "El usuario no ha sido encontrado con ese id"
		respuesta = {"result":result,"mensajes":mensajes, "usuario":usuarioEncontrado}
		return respuesta