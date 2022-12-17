import os
from flask_dotenv import DotEnv
from termcolor import colored

from flask_sqlalchemy import SQLAlchemy

class DB:

	db = None
	
	def __init__(self):
		print(colored("DB: __init__()", 'yellow'))

	@staticmethod
	def iniciarConApp(app):
		print(colored("DB: iniciarConApp()", 'yellow'))
		DB.db = SQLAlchemy(app)
		if(DB.db is not None):
			print(colored("DB: iniciada con éxito", 'yellow'))

	@staticmethod
	def obtener():
		#print(colored("DB: obtener()", 'yellow'))
		if (DB.db is None):
			print(colored("DB: obtener() DB es None", 'red'))
			raise Exception("DB: obtener() DB es None")
		else:
			return DB.db