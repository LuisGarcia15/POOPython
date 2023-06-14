# import aritmetica as ari
# puedes colocarle un alias, solo que de esa forma
# debes especificar que las funciones (o código que se necesite
# como una clase)usadas provienen de esa clase ari.suma(1,1)

from aritmetica import suma,resta
# Lo menor es importar todas las funciones
# de manera explicita para no tener que colocar
# un alias cada que necesites usar una funcion
# de la claese importada
def main():
    resultado = suma(None, None)
    resultado2 = resta(b = 5, a = 3)
    print(resultado)
    print(resultado2)

main()