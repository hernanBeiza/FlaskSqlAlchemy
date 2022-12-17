from termcolor import colored

from src.DB import DB

from src.DAOS.Models.Tarea import Tarea

class TareaDAO():

	'''
	def __init__(self):
		print('TareaDAO')
	'''

	@staticmethod
	def guardar(tareaVO):
		print(colored("TareaDAO: guardar(); {}".format(tareaVO.idusuario), 'yellow'))
		tarea = Tarea(None, tareaVO.titulo, 2, tareaVO.idusuario)
		DB.obtener().session.add(tarea)
		result=True
		mensajes="Tarea guardada correctamente"
		try:
			DB.obtener().session.commit()
			print(colored("TareaDAO: tarea guardada correctamente", 'yellow'))
			#usuario = Usuario.query.get(usuario.idusuario)
			respuesta = {"result":result,"mensajes":mensajes, "tarea":tarea}
		except Exception as e:
			print (e)
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			DB.obtener().session.rollback()
			# for resetting non-commited .add()
			DB.obtener().session.flush()
			result=False
			mensajes="La tarea no se pudo guardar"
			respuesta = {"result":result,"errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("TareaDAO: obtener();", 'yellow'))		
		return Tarea.query.all()

	@staticmethod
	def obtenerConPagina(pagina):
		print(colored("TareaDAO: obtenerConPagina(); {}".format(pagina), 'yellow'))
		totalPorPagina = 2
		return Tarea.query.paginate(pagina,int(totalPorPagina), False)

	@staticmethod
	def obtenerConID(idTarea):
		print(colored("TareaDAO: obtenerConID(); {}".format(idTarea), 'yellow'))
		return Tarea.query.get(idTarea)

	@staticmethod
	def obtenerConIDUsuario(idUsuario):
		print(colored("TareaDAO: obtenerConIDUsuario(); {}".format(idUsuario), 'yellow'))
		return Tarea.query.filter_by(idusuario=idUsuario).all()

	@staticmethod
	def editar(tareaVO):
		print(colored("TareaDAO: editar(); {}".format(tareaVO.idtarea), 'yellow'))
		result=True
		mensajes="Tarea editada correctamente"
		try:
			tarea = Tarea.query.get(tareaVO.idtarea)
			tarea.titulo = tareaVO.titulo;
			tarea.idusuario = tareaVO.idusuario;
			tarea.valid = tareaVO.valid;
			DB.obtener().session.commit()
			respuesta = {"result":result,"mensajes":mensajes, "tarea":tarea}
		except Exception as e:
			print (e)
			#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
			DB.obtener().session.rollback()
			# for resetting non-commited .add()
			DB.obtener().session.flush()
			result=False
			mensajes="La tarea {} no se pudo editar".format(tareaVO.idtarea)
			respuesta = {"result":result,"errores":mensajes}
		return respuesta

	@staticmethod
	def eliminar(idTarea):
		result = True
		mensajes = "Tarea con id {} eliminada correctamente".format(idTarea)
		tarea = Tarea.query.get(idTarea)
		if(tarea is not None):
			try:
				DB.obtener().session.delete(tarea)
				DB.obtener().session.commit()
				respuesta = {"result":result,"mensajes":mensajes}
				return respuesta
			except Exception as e:
				print ("Error al eliminar la tarea con id {}. Error: {}".format(idTarea, e))
				#log your exception in the way you want -> log to file, log as error with default logging, send by email. It's upon you
				DB.obtener().session.rollback()
				# for resetting non-commited .add()
				DB.obtener().session.flush()
				result=False
				mensajes="La tarea con id {} no se pudo eliminar".format(idTarea)
		else:
			result=False
			mensajes="La tarea con id {} no se ha podido encontrar".format(idTarea)

		respuesta = {"result":result,"errores":mensajes}
		return respuesta
