from ..app import app;

from ..Services.IndexService import IndexService

class IndexController():

	@app.route('/', endpoint='/', methods = ['GET'])
	def saludar():
		return IndexService().saludar()