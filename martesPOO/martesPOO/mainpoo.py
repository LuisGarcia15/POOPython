from cosas import Alumno

def main():
    """
    al1 = Alumno() #Constructor
    #print(al1)
    al2 = Alumno('Juan', 'ICO')
    print(al1.facultad)
    print(al2.facultad)
    print(Alumno.facultad)
    print('----')
    al1.facultad = "Fes Aragon EdoMex" #Se agrega una variable
    # De instancia al objeto al1
    print(al1)
    print(al2)
    print(Alumno.facultad)
    print('--- Vistaso a los objetos')
    # vars() permite observar las variables de instancia
    # de un objeto dado como parámetro
    print(vars(al1))
    print(vars(al2))
    # Para cambiar un atributo de clase se realiza
    Alumno.facultad = "CU"
    """
    al1 = Alumno('Luis', 21, 'ICO')
    al2 = Alumno('Juan', 22, 'Derecho')
    #print(al1.nombre)
    print(al1.facultad)
    #print(al2.nombre)
    print(al2.facultad)
    print(vars(al1))
    print(vars(al2))
    al3 = Alumno('Alex', 23, 'Periodismo')
    print(vars(al3))
    al3.__edad = 999
    #Si bien no se modifica la variable edad que se esperaba
    # si se crea una nueva variable edad que tiene el dato de 999
    # esto se comprueba con el método vars()
    print(vars(al3))
main()