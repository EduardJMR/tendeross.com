from app import database

class Rol (database.Model):
    
    __tablename__ = 'roles'
    
    id= database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)