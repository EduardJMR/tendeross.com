from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Hello World </h1>"

@app.route('/login')
def login():
    return "<h1> Iniciar Sesión </h1>"