# Python usa como nomenclatura
# de notación snake_case
class Alumno:
    facultad = "FES Aragón"

    def __init__(self, nom, ed, carr):
        # self: Recibe de manera implicita el objeto que lo llama

        #.__: si se le coloca a una variable de instancia
        # simula el encapsulamiento
        self.__nombre = nom
        self.__edad = self.set_edad(ed)
        self.__carrera = carr

    # horas = 1, indica que si no se provee un
    # argumento para el parámetro horas, se toma
    # de manera automática, el valor que se asigne
    # como default
    def estudiar (self, horas = 1):
        print(f"El alumno {self.__nombre} esta estudiando por {horas} horas")

    def set_nombre(self, nombre):
        #Notación Snake Case
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if edad >= 8 and edad < 120:
        #Notación Snake Case
            self.__edad = edad
        else:
            # raise, palabra reservada
            # para lanzar una excepción
            print("La edad no es correcta")
            self.__edad = 0

    def get_edad(self):
        return self.__edad

    def set_carrera(self, carrera):
        #Notación Snake Case
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def __str__(self):
        cadena = "nombre: [" + self.__nombre + "] \nedad: [" + str(self.__edad) + "] \ncarrera: [" + self.__carrera + "]"
        return cadena

# Una modulo en Python puede contener varias
# definiciones de clases
class Perro:

    reino = "Canino"

    def __init__(self, raza, edad, estatura):
        self.__raza = raza
        self.__edad = edad
        self.__estatura = estatura

    @staticmethod
    def es_cachorro(edad):
        return edad < 3

    @staticmethod #No puede acceder ni a los atributos
    # de la clase ni a lo atributos de las instancias
    def dormir(veces_vueltas = 5):
        for n in range(veces_vueltas):
            print(f"Dando vuelta {n + 1}")
        print("Zzzzzz!")

    @classmethod #Puede acceder a los atributos de la clase
    # cls: Recibe de manera implicita la clase que lo llama
    # Permite sobrecargar constructores
    def perro_grande(cls, estatura):
        if estatura > 0.7:
            return cls("", 0, estatura)

    @classmethod
    def constructor_dos(cls, raza, edad):
        if edad > 0 and edad < 20:
            return cls(raza, edad, 0.0)
        else:
            return cls(raza,0,0.0)

    @property
    # Decorador que permite crear un método
    # get de una variable de instanicia, respetando
    # las reglas de escritura de python. Siempre
    # y cuando el método se llame igual a la variable
    # de intancia
    def raza(self):
        return self.__raza

    @raza.setter
    # Decorador que, un vez creado el método get con
    # el decorador property, permite crear el método
    # setter de la variable de intancia. Este decorador y
    # esta creación de set solo puede usarse si anteriormente
    # se creo el método get de la variable de instancia. Tambíen
    # el método debe llamarse igual que la variable de instancia
    def raza(self, raza):
        self.__raza = raza

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if edad > 0 and edad < 20:
            self.__edad = edad
        else:
            print(f'{edad}: no es una edad valida')
            self.__edad = 0

    @property
    def estatura(self):
        return self.__estatura

    @estatura.setter
    def estatura(self, estatura):
        if estatura >= 0.1 and estatura < 1.1:
            self.__estatura = estatura
        else:
            print(f'{estatura}: no es una estatura valida')
            self.__estatura = 0.1

    def __str__(self):
        return f"""
 ---------------------------
Raza: [{self.__raza}]
Edad: [{self.__edad}]
Estatura [{self.__estatura}]
 ---------------------------
        """


