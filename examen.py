animal="León"
def mostrar_animal():
    """Esta funcion muestra el valor de la variable animal por consola"""
    global animal
    animal="Ballena"
    print(animal)

    mostrar_animal()
    print(animal)