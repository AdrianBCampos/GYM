from logica.Usuario import Usuario

class Empleado (Usuario):
    def __init__(self, idTurno, idPuesto, id, usuario, contraseña, nombre, apellido, dni, fechaNac, genero, domicilio, email, tel):
        super().__init__(id, usuario, contraseña, nombre, apellido, dni, fechaNac, genero, domicilio, email, tel)
        self.idTurno = idTurno
        self.idPuesto = idPuesto
        
    def MostrarInfo(self):
        return super().MostarInfo() + self.__idTurno + self.__idPuesto   
    
    
