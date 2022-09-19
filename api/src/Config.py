from flask_dotenv import DotEnv
from termcolor import colored

class Config:

	@staticmethod
	def init_app(app):
		#print("Config: init_app")
		#Configuracion de Flask
		print(colored("Iniciar configuración de Flash", 'yellow'))
		app.config['JSON_SORT_KEYS'] = False
		#Variables de ambiente
		env = DotEnv()
		ruta = "src/config/development.env"
		print(colored("Cargar archivo según ambiente {}".format(ruta), 'yellow'))
		env.init_app(app, env_file=ruta, verbose_mode=True)
		