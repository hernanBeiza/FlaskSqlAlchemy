from src.app import app

from src.Services.IndexService import IndexService

@app.route('/', endpoint='/', methods = ['GET'])
def saludar():
	return IndexService().saludar()