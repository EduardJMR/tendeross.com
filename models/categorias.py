from app import database

class Categoria (database.Model):
    
    __tablename__ = 'categorias'
    
    id= database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)