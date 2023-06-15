from cosas import Alumno, Perro

def main():
    al1 = Alumno('Jose', 19, 'ICO')
    print(vars(al1))
    al1.__nombre = "Diego"
    # Crea una variable adicional aun si ya
    # Existe una variable de instancia con
    # nombre igual. Esto para simular el
    # encapsulamiento. Si se requiere el
    # encapsulamiento total, debemos crear
    # los métodos de acceso (get y set)
    print(vars(al1))
    al1.set_nombre("Luis")
    print(vars(al1))
    print('-----To string ------')
    print(al1)
    al1.estudiar(4)
    print('----- Perro -----')
    perro1 = Perro('Poddle', 2, 0.35)
    print(vars(perro1))
    perro1.raza = 'Calle' #Set en notación Pythonic
    print(vars(perro1))
    print(Perro.es_cachorro(perro1.edad))
    Perro.dormir(3)
    danes = Perro.perro_grande(0.8)
    print(danes)
    print("----- @classmethod -----")
    perro2 = Perro("Pug", 1, 0.4)
    perro3 = Perro.perro_grande(0.9)
    perro4 = Perro.constructor_dos("Chihuahua", 23)
    print(perro2)
    print(perro3)
    print(perro4)

main()