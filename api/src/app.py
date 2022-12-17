import flask
from termcolor import colored

from src.Config import Config
from src.DB import DB

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#print("app.py");
app = flask.Flask(__name__)
#
Config.iniciarConApp(app);
#app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlconnector://root:0C3v8ea0@192.168.56.101/tareadb'
#
#db = SQLAlchemy(app)
DB.iniciarConApp(app)
#
ma = Marshmallow(app)

from .routes import *
#import routes;

#app.run(host='localhost', port=3000)