import os
from flask_dotenv import DotEnv
from termcolor import colored

class Config:

	def __init__(self):
		print(colored("Config: __init__()", 'yellow'))

	@staticmethod
	def iniciarConApp(app):
		print(colored("Config: iniciarConApp()", 'yellow'))
		#Configuracion de Flask
		print(colored("Config: Iniciar configuración de Flash", 'yellow'))
		app.config['JSON_SORT_KEYS'] = False
		#Variables de ambiente
		environment = os.environ.get("FLASK_ENV")
		print(colored("Config: Cargar archivo según ambiente: {}".format(environment), 'yellow'))
		env = DotEnv()
		ruta = "src/config/.env.{}".format(environment)
		print(colored("Config: Archivo a cargar según ambiente: {}".format(ruta), 'yellow'))
		env.init_app(app, env_file=ruta, verbose_mode=True)