from .TareaVOBuilder import TareaVOBuilder

class VOBuilderFactory():

	#def __init__(self):

	@staticmethod
	def VOBuilderFactory():
		print("VOBuilderFactory")

	@staticmethod
	def getTareaVOBuilder():
		return TareaVOBuilder()
