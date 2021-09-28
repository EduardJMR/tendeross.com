from app import database

class Tienda (database.Model):
    
    __tablename__ = 'tiendas'
    
    id= database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    logo = database.Column(database.String, nullable=False)
    direccion = database.Column(database.String, nullable=False)
    ciudad = database.Column(database.String, nullable=False)
    celular = database.Column(database.Integer, nullable=False)
    nit = database.Column(database.String, nullable=False)
    productos = database.Column(database.Integer, nullable=False)