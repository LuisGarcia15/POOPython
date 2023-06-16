class Persona:
    # En herencia multiple, siempre que se llame a un constructor
    # de una super clase o se llame a un método de una superclase
    # es necesario colocar como primer parámetro la palabra reservada
    # self, pues se le debe de pasar como parametro (de manera explicita)
    # el objeto con el que se trabaja

    descripcion = "un ser humano común y corriente"

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nom):
        self.__nombre = nom

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, ed):
        self.__edad = ed

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad}"

    def dormir(self):
        print("ZzZzZzZzZzZz que calors.... zZzz")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0)


class Alumno(Persona):
    descripcion = "Una persona que dice que estudia pero se la pasa en el cel"

    def __init__(self, nombre, edad, nc, carrera):
        # Es necesario enviar el objeto de manera explicita con self
        # por ello, en un constructor de herencia multiple, debe colocarse
        # de manera explicita self
        Persona.__init__(self, nombre, edad)
        # Dado que al llamar al constructor en herencia multiple se utiliza
        # explicitamente la clase y tambien se utiliza para llemar métodos de
        # las super clase, es necesario colocar de manera explicita self, dado
        # que debemos de pasar explicitamente el objeto con el que se trabaja
        # esto bajo la palabra reservada self
        self.__numero_cuenta = nc
        self.__carrera = carrera

    @property
    def numero_cuenta(self):
        return self.__numero_cuenta

    @numero_cuenta.setter
    def numero_cuenta(self, nc):
        self.__numero_cuenta = nc

    @property
    def carrera(self):
        return self.__carrera

    @carrera.setter
    def carrera(self, carrera):
        self.__carrera = carrera

    def __str__(self):
        return super().__str__() + f", Numero de cuenta: {self.__numero_cuenta}, Carrera: {self.__carrera}"

    def dormir(self):
        print(super().nombre, " está durmiendo como alumno")

    @classmethod
    def constructor_defecto(cls):
        return cls("", 0, "", "")


class Profesor(Persona):
    descripcion = "Una persona que dice que enseña pero se la pasa leyendo artículos de investigación"

    def __init__(self, nombre, edad, num_tra, area):
        # Dado que al llamar al constructor en herencia multiple se utiliza
        # explicitamente la clase y tambien se utiliza para llemar métodos de
        # las super clase, es necesario colocar de manera explicita self, dado
        # que debemos de pasar explicitamente el objeto con el que se trabaja
        # esto bajo la palabra reservada self
        Persona.__init__(self, nombre, edad)
        # Es necesario enviar el objeto de manera explicita con self
        # por ello, en un constructor de herencia multiple, debe colocarse
        # de manera explicita self
        self.__numero_trabajador = num_tra
        self.__area = area

    @property
    def numero_trabajador(self):
        return self.__numero_trabajador

    @numero_trabajador.setter
    def numero_trabajador(self, num_tra):
        self.__numero_trabajador = num_tra

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def __str__(self):
        return super().__str__() + f", Numero de trabajador: {self.__numero_trabajador}, Area: {self.__area}"

    def dormir(self):
        print(super().nombre, " está durmiendo como profesor")

class AyudanteProfsesor(Alumno,Profesor):

    def __init__(self, nombre, edad, numero_cuenta, carrera, numero_trabajador, area, numero_horas):
        # Como se hereda de multiples clases, es imposible utilizar super()
        # Para referirnos al constructor de la super clase, es por eso que
        # en la herencia múltiple se utiliza explicitamente el nombre de la clase
        # de la cual heredas, seguido de su constructor

        # Es necesario enviar el objeto de manera explicita con self
        # por ello, en un constructor de herencia multiple, debe colocarse
        # de manera explicita self
        Alumno.__init__(self, nombre, edad, numero_cuenta, carrera)
        # Dado que al llamar al constructor en herencia multiple se utiliza
        # explicitamente la clase y tambien se utiliza para llemar métodos de
        # las super clase, es necesario colocar de manera explicita self, dado
        # que debemos de pasar explicitamente el objeto con el que se trabaja
        # esto bajo la palabra reservada self
        Profesor.__init__(self, nombre, edad, numero_trabajador, area)
        self.__numero_horas = numero_horas

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

        @property
        def numero_cuenta(self):
            return self.__numero_cuenta

        @numero_cuenta.setter
        def numero_cuenta(self, numero_cuenta):
            self.__numero_cuenta = numero_cuenta

        @property
        def carrera(self):
            return self.__carrera

        @carrera.setter
        def carrera(self, carrera):
            self.__carrera = carrera

        @property
        def numero_trabajador(self):
            return self.__numero_trabajador

        @numero_trabajador.setter
        def numero_trabajador(self, numero_trabajador):
            self.__numero_trabajador = numero_trabajador

        @property
        def area(self):
            return self.__area

        @area.setter
        def area(self, area):
            self.__area = area

        @property
        def numero_horas(self):
            return self.__numero_horas

        @numero_horas.setter
        def numero_horas(self, numero_horas):
            self.__numero_horas = numero_horas

        def __str__(self):
            # Dado que al llamar al constructor en herencia multiple se utiliza
            # explicitamente la clase y tambien se utiliza para llemar métodos de
            # las super clase, es necesario colocar de manera explicita self, dado
            # que debemos de pasar explicitamente el objeto con el que se trabaja
            # esto bajo la palabra reservada self
            return Alumno.__str__(self) + Profesor.__str__(self) + f"Horas de trabajo: {self.horas}"

        def dar_clase(self, materia):
            # Dado que ya esta encapculado por la herencia, no es necesario colocar los dobles guiones
            # bajos entre self. y el nombre de la variable
            print(f"{self.nombre} esta dando {materia} del area {self.area} por {self.horas} horas")

        def dormir(self):
            super().dormir()