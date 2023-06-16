from cosas import *

def main():
    persona1 = Persona("José", 19)
    print(persona1)
    print(Persona.descripcion)
    print("---- Herencia Alumno ----")
    alumno1 = Alumno("Jose", 19,"22319543", "ICO")
    print(alumno1)
    print(alumno1.descripcion)
    alumno2 = Alumno.constructor_defecto()
    print(alumno2)
    alumno2.nombre = "Juan"
    print(alumno2)
    alumno2.dormir()
    print('---- Herencia profesor ----')
    profesor1 = Profesor('Jesús', 46, 323253, "Ingeniería de Software")
    print(profesor1)
    profesor1.dormir()
    print('---- Herencia Ayudante de Profesor ----')
    ayudante = AyudanteProfsesor("Adrian", 20, "25252", "ICO", 23223, "Ingeniería de Software", 4)
    print(ayudante)
    ayudante.dormir()
main()