from flask import request
from flask import escape
from flask import json
from flask import jsonify
from flask import Blueprint

from termcolor import colored
from ..app import db

from ..DAOS.TareaDAO import TareaDAO

from .VOS.TareaVO import TareaVO
from .Builder.VOBuilderFactory import VOBuilderFactory

class TareaService():

	"""
	def __init__(self):
		print('TareaService')
	"""
	
	@staticmethod
	def guardar(request):
		print(colored("TareaService: guardar(); {}".format(request.form), 'cyan'))
		titulo = request.form.get("titulo")
		idUsuario = request.form.get("idUsuario")
		enviar = True
		mensajes = "Te falta:"
		if(titulo==None):
			enviar = False
			mensajes +="\nTítulo"
		if(idUsuario==None):
			enviar = False
			mensajes +="\nid de usuario"

		if(enviar):
			tareaVO = TareaVO()
			tareaVO.titulo = titulo
			tareaVO.idusuario = idUsuario
			respuesta = TareaDAO.guardar(tareaVO)
			print(colored(respuesta, 'cyan'))
			if(respuesta["result"]):
				tarea = VOBuilderFactory.getTareaVOBuilder().fromTarea(respuesta["tarea"]).build()
				respuesta["tarea"] = tarea
			else:
				respuesta = {"result":False, "errores":respuesta["mensajes"]}
		else:
			respuesta = {"result":False, "errores":mensajes}
		return respuesta

	@staticmethod
	def obtener():
		print(colored("TareaService: obtener();", 'cyan'))
		tareas = TareaDAO.obtener()
		if len(tareas)>0:
			data = {
				"result":True,
				"tareas":VOBuilderFactory.getTareaVOBuilder().fromTareas(tareas).builds(),
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
				"tareas":VOBuilderFactory.getTareaVOBuilder().fromTareas(paginacion.items).builds(),
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
				"tarea":VOBuilderFactory.getTareaVOBuilder().fromTarea(tarea).build(),
				"mensajes":"Se encontró tarea con id {}".format(idTarea)
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
			"tareas":VOBuilderFactory.getTareaVOBuilder().fromTareas(tareas).builds(),
			"mensajes":"Se encontraron {} tareas para el usuario con id {}".format(len(tareas),idUsuario)
		}
		return data

	@staticmethod
	def editar(request):
		print(colored("TareaService: editar(); {}".format(request.form), 'cyan'))
		titulo = request.form.get("titulo")
		idUsuario = request.form.get("idUsuario")
		valid = request.form.get("valid")
		idTarea = request.form.get("idTarea")
		enviar = True
		mensajes = "Te faltó:"
		if(titulo==None):
			enviar = False
			mensajes +="\nTítulo"
		if(idUsuario==None):
			enviar = False
			mensajes +="\nidUsuario"
		if(idTarea==None):
			enviar = False
			mensajes +="\nID de la tarea a editar"
		if(valid==None):
			enviar = False
			mensajes +="\nValid"

		if(enviar):
			tareaVO = TareaVO()
			tareaVO.idtarea = idTarea
			tareaVO.idusuario = idUsuario
			tareaVO.titulo = titulo
			tareaVO.valid = valid
			respuesta = TareaDAO.editar(tareaVO)
			print(colored(respuesta, 'cyan'))
			if(respuesta["result"]):
				tareaVO = VOBuilderFactory().getTareaVOBuilder().fromTarea(respuesta["tarea"]).build()
				respuesta["tarea"] = tareaVO
			else:
				return {"result":False, "errores":respuesta["mensajes"]}
		else:
			return {"result":False, "errores":mensajes}

		return respuesta

	@staticmethod
	def eliminar(idTarea):
		print(colored("TareaService: eliminar(); {}".format(idTarea), 'cyan'))
		return TareaDAO.eliminar(idTarea)
