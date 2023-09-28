from logica.Usuario import Usuario
from logica.Empleado import Empleado


yo = Usuario (1,"adri","latorre", "Adrian", "Campos", 24821072, "17/08/75", "H", "Varela 1460", "adri@gmail.com", 1135794494)

print ("Datos del usuario:\n ")
print (yo.MostrarInfo())
yo.CambiarDomicilio("Av. Rivadavia 1001")
print ("Datos del usuario:\n ")
print (yo.MostrarInfo())


#////////////////////////////////////////
#LOGIN
#///////////////////////////////////////

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#CREO EL MENÚ PRINCIPAL 
bucle =0
opcion =0
while bucle !=1:
  try:
    opcion = int(input("Ingrese una opción: \n 1- Menú clases\n 2- Menú entrenamientos personalizados\n 3- Salir\n"))  
    
  except ValueError:
    print("Se ingresó mal la opción.  Vuelva a intenrar.")
  if opcion == 1:
    yo = Empleado ("Juan")
    yo.Menu()
  elif opcion == 2:
    yo = Empleado ("Juan")
    yo.Menu()
  elif opcion == 3:
    bucle = 1
print ("Final") 