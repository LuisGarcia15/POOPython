class Autor:
    def __init__(self, nombre, pseudonimo):
        self.__nombre = nombre
        self.__pseudonimo = pseudonimo

    def escribir(self):
        print(f"{self.__pseudonimo} está escribiendo su siguiente obra")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def pseudonimo(self):
        return self.__pseudonimo

    @pseudonimo.setter
    def pseudonimo(self, pseudonimo):
        self.__pseudonimo = pseudonimo

    def __str__(self):
        return f"Nombre: [{self.__nombre}] - Pseudonimo: [{self.__pseudonimo}]"

class Libro:

    def __init__(self, titulo, autor, anio, editorial):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__editorial = editorial

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
            return self.__autor

    @autor.setter
    def nombre(self, autor):
            self.__autor = autor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, anio):
        self.__anio = anio

    @property
    def editorial(self):
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial):
        self.__editorial = editorial

    @classmethod
    def libro_planeta(cls, titulo, autor, año):
        return cls(titulo, autor, año, "Planeta")

    def leer(self, minutos):
        print(f"Leyendo por {minutos} minutos")

    def __str__(self):
        return \
f"""
---------
Titulo: [{self.__titulo}]
Autor: [{self.__autor}]
Año: [{self.__anio}]
Editorial: [{self.__editorial}]
---------
"""

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    def __str__(self):
        return f"""
-------------
Nombre : [{self.__nombre}]
Edad : [{self.__edad}]
------------
"""

class Alumno(Persona):

    def __init__(self, nombre, edad, numero_cuenta, carrera, promedio):
        # super(): Función especial que es obligatoria escribirla
        # pues llama al constructor de la clase padre de la que hereda
        # la subclase
        super().__init__(nombre, edad)
        self.__numero_cuenta = numero_cuenta
        self.__carrera = carrera
        self.__promedio = promedio

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, numero_cuenta):
        self.__numero_cuenta = numero_cuenta

    @property
    def  carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    @property
    def promedio(self):
        return self.__promedio

    @promedio.setter
    def promedio(self, promedio):
        self.__promedio = promedio

    def __str__(self):
        return f"""
    -------------
    Nombre : [{super().nombre}]
    Edad : [{super().edad}]
    Número de cuenta : [{self.__numero_cuenta}]
    Carrera : [{self.__carrera}]
    Promedio : [{self.__promedio}]
    ------------
    """



