from src.app import app

class IndexService():

	def __init__(self):
		print('IndexService __init__()')

	@staticmethod
	def saludar():
		return {"result":True,"mensaje":"Bienvenido a la API de Tareas","version":app.config["VERSION"]}