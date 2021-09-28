from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kbalvhbvezzejl:f8530c879cf80bf6fbeb4cb24f63faaa470ea956c533efdf1533924b942997cc@ec2-3-219-111-26.compute-1.amazonaws.com:5432/dfiftl9067ie8d'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)
from models.usuarios import Usuario

@app.route('/')
def home():
    correos = ''
    usuarios = Usuario.get_all()
    for user in usuarios:
        correos += user.correo + ' '
        print (user.correo)
    
    return Usuario.get_id().correo

@app.route('/login')
def login():
    return "<h1> Iniciar Sesión </h1>"