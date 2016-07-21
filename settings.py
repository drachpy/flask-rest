from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)
db = SQLAlchemy(app)
