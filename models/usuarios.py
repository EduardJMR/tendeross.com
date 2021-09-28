from app import database

class Usuario(database.Model):
    
    __tablename__ = 'usuarios'
    
    id_usuario = database.Column(database.Integer, primary_key=True)
    nombre = database.Column(database.String, nullable=False)
    correo = database.Column(database.String, nullable=False)
    contraseña = database.Column(database.String, nullable=False)
    
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    @staticmethod
    def get_id():
        return Usuario.query.filter_by(id_usuario = 2).first()