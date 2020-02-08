from flask_dotenv import DotEnv

class Config:

	@classmethod
	def init_app(self, app):
		print("Config: init_app")
		print(app.config)
		env = DotEnv()
		env.init_app(app, env_file="development.env", verbose_mode=True)
		print(app.config)