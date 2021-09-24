from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://kbalvhbvezzejl:f8530c879cf80bf6fbeb4cb24f63faaa470ea956c533efdf1533924b942997cc@ec2-3-219-111-26.compute-1.amazonaws.com:5432/dfiftl9067ie8d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/login')
def login():
    return "<h1> Iniciar Sesión </h1>"