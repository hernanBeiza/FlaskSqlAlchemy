from ..app import db

from termcolor import colored

from ..DAOS.Models.Tarea import Tarea
from ..DAOS.Schemas.TareaSchema import TareaSchema
from ..DAOS.TareaDAO import TareaDAO

from .VOS.TareaVO import TareaVO

class TareaService():

	"""
	def __init__(self):
		print('TareaService')
	"""
	
	@staticmethod
	def guardar(tareaVO):
		print(colored("TareaService: guardar(); {}".format(tareaVO.idusuario), 'cyan'))
		respuesta = TareaDAO.guardar(tareaVO)
		print(colored(respuesta, 'cyan'))
		if(respuesta["result"]):
			tarea = TareaSchema().dump(respuesta["tarea"])
			respuesta["tarea"] = tarea
		return respuesta

	@staticmethod
	def obtener():
		print(colored("TareaService: obtener();", 'cyan'))
		tareas = TareaDAO.obtener()
		if len(tareas)>0:
			data = {
				"result":True,
				"tareas":TareaSchema(many=True).dump(tareas),
				"mensajes":"Se encontraron {} tareas".format(len(tareas))
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tareas"
			}
		return data

	@staticmethod
	def obtenerConPagina(pagina):
		print(colored("TareaService: obtenerConPagina();", 'cyan'))
		paginacion = TareaDAO.obtenerConPagina(pagina)
		if len(paginacion.items)>0:
			data = {
				"result":True,
				"totalPaginas":paginacion.pages,
				"actualPagina":paginacion.page,
				"tareas":TareaSchema(many=True).dump(paginacion.items),
				"mensajes":"Se encontraron {} tareas".format(len(paginacion.items))
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tareas"
			}
		return data

	@staticmethod
	def obtenerConID(idTarea):
		print(colored("TareaService: obtenerConID();", 'cyan'))
		tarea = TareaDAO.obtenerConID(idTarea)	
		if tarea is not None:
			data = {
				"result":True,
				"tareas":TareaSchema(many=False).dump(tarea),
				"mensajes":"Se encontró tarea con id {}".format(len(idTarea))
			}
		else:
			data = {
				"result":False,
				"errores":"No se encontraron tarea con id {}".format(idTarea)
			}
		return data

	@staticmethod
	def obtenerConIDUsuario(idUsuario):
		print(colored("TareaService: obtenerConIDUsuario();", 'cyan'))
		tareas = TareaDAO.obtenerConIDUsuario(idUsuario)
		data = {
			"result":len(tareas) > 0,
			"tareas":TareaSchema(many=True).dump(tareas),
			"mensajes":"Se encontraron {} tareas para el usuario con id {}".format(len(tareas),idUsuario)
		}
		return data

	@staticmethod
	def editar(tareaVO):
		print(colored("TareaService: editar(); {}".format(tareaVO.idtarea), 'cyan'))
		respuesta = TareaDAO.editar(tareaVO)
		print(colored(respuesta, 'cyan'))
		if(respuesta["result"]):
			tarea = TareaSchema().dump(respuesta["tarea"])
			respuesta["tarea"] = tarea
		return respuesta

	@staticmethod
	def eliminar(idTarea):
		print(colored("TareaService: eliminar(); {}".format(idTarea), 'cyan'))
		return TareaDAO.eliminar(idTarea)
