from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "IITMBS21"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['UPLOAD_FOLDER'] = 'static/uploads/'
api = Api(app)
db = SQLAlchemy(app)
