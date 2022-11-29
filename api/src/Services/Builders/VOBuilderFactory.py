from src.Services.Builders.TareaVOBuilder import TareaVOBuilder
from src.Services.Builders.UsuarioVOBuilder import UsuarioVOBuilder

class VOBuilderFactory():

	#def __init__(self):

	@staticmethod
	def VOBuilderFactory():
		print("VOBuilderFactory")

	@staticmethod
	def getTareaVOBuilder():
		return TareaVOBuilder()

	@staticmethod
	def getUsuarioVOBuilder():
		return UsuarioVOBuilder()
