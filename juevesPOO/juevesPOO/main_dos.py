from cosas_dos import *

def main():
    l1 = Libro.libro_planeta("El perfume", Autor("Patrick", "PS"), 1980)
    print(l1)
    # código para cambiar pseudonimo a minusculas
    l1.autor.pseudonimo = l1.autor.pseudonimo.lower()
    print(l1)
    print('------- Herencia ---------')
    al1 = Alumno("Jose", 19, "122312", "ICO", 9.0)
    al1.nombre = "Pepe"
    print(al1)


main()