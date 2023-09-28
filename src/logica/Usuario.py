

class Usuario:
    def __init__(self,id, usuario, contraseña, nombre, apellido, dni, fechaNac, genero, domicilio, email, tel):
        self.__id = id
        self.__usuario = usuario
        self.__contraseña = contraseña
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__fechaNac = fechaNac
        self.__genero = genero
        self.__domicilio = domicilio
        self.__email = email
        self.__tel = tel
        
    def MostrarInfo(self):
        return "Nombre: ",self.__nombre, "\nApellido: ", self.__apellido, "\nDNI: ", self.__dni, "\nFecha de nacimiento: ",self.__fechaNac,"\nGenero: ",self.__genero, "\nDomicilio: ",self.__domicilio, "\nE-mail: ",self.__email, "\nTeléfono: ",self.__tel,"\n "
        
    def CambiarDomicilio(self,domicilio):
        self.__domicilio = domicilio 
        
   
        
    
        



    

