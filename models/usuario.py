from app import database

class Usuarios(database.Model):
    
    __tablename__ = 'usuarios'
    
    id_usuario = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    correo = database.Column(database.String, nullable=False)
    contraseña = database.Column(database.String, nullable=False)