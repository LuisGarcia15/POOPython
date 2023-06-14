class Alumno:
    #variable de clase: sin aquellas que estan fuera de los
    #métodos, regularmente se usa cuando esa variables es
    #común en todos los objetos
   facultad = 'Fes Aragon'
   #def __init__(self):#Constructor de una clase en Python
       # print(type(self))
        # pass Palabra reserfva para indicar que el método
        #no hace nada, pero existe para que no salte un error

        #self, equivalente a this en Java. Sin embargo, el objeto
        #en uso se envia como argumento por medio del parámetro self
        #para emular POO

   def __init__(self, nombre, edad,carrera):
        #print(type(self))
        self.__nombre = nombre
        self.__edad = edad
        self.__carrera = carrera
        # Colocar dos guiones bajos antes de una variable de instancia
        # es como simula el encapsulamiento (como private en java)