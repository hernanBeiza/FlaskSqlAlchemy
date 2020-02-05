from ..app import app;

from ..Services.IndexService import IndexService

@app.route('/', endpoint='/', methods = ['GET'])
def saludar():
	return IndexService().saludar()