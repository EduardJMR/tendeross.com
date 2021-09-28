from app import database

class Producto (database.Model):
    
    __tablename__ = 'productos'
    
    id= database.Column(database.Integer, primary_key=True)
    codigo= database.Column(database.Integer, nullable=False)
    nombre = database.Column(database.String, nullable=False)
    descripcion = database.Column(database.String, nullable=False)
    imagen = database.Column(database.String, nullable=False)
    categoria = database.Column(database.Integer, nullable=False)
    valor_compra = database.Column(database.Integer, nullable=False)
    valor_venta = database.Column(database.Integer, nullable=False)
    stock = database.Column(database.Integer, nullable=False)
    stock_minimo = database.Column(database.Integer, nullable=False)
    estado = database.Column(database.Boolean, nullable=False)