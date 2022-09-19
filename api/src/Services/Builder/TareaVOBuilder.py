from ..vos.TareaVO import TareaVO

class TareaVOBuilder():

	tarea = None

	#def __init__(self):

	@staticmethod
	def fromTarea(tarea):
		TareaVOBuilder.tarea = tarea
		return TareaVOBuilder()

	@staticmethod
	def build():		
		if(TareaVOBuilder.tarea is None):
			print("No se puede contruir TareaVO")
			return None
		else:
			tareaVO = TareaVO()
			tareaVO.idTarea = TareaVOBuilder.tarea.idtarea
			tareaVO.titulo = TareaVOBuilder.tarea.titulo
			tareaVO.timestamp = TareaVOBuilder.tarea.timestamp
			tareaVO.valid = TareaVOBuilder.tarea.valid
			return tareaVO
