from src.app import app;

from src.Services.IndexService import IndexService

class IndexController():

	@app.route('/', endpoint='/', methods = ['GET'])
	def saludar():
		return IndexService().saludar()