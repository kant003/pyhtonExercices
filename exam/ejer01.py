# -*- coding: utf-8 -*-
# Crea una función a la que le pases un Set, una lista, una tupla o un número(entero o decimal), y determine:
#  - si alguno de los elementos de la colección contiene el número 13 (en caso de pasarsele un set, lista o tupla)
#  - o si el numero pasado es 13, en caso de pasarsele un número
# La función debe llamarse bad_luck(data)
# Donde data podrá ser de tipo lista, tupla, set, un entero o un decimal, en caso de no serlo se devolverá None

def bad_luck(data):
    # tu código aquí

def test():
    assert bad_luck({2,13,5}) == True, "{2,13,5} Should be True"
    assert bad_luck([2,5]) == False, "[2,5] Should be False"
    assert bad_luck((2,5)) == False, "(2,5) Should be False"
    assert bad_luck((2,5,13)) == True, "(2,5,13) Should be True"
    assert bad_luck((2,4)) == False, "(2,4) Should be False"
    assert bad_luck('casa') == None, "casa Should be None"
    assert bad_luck(None) == None, "None Should be None"
    assert bad_luck(34) == False, "34 Should be False"
    assert bad_luck(34.8) == False, "34.8 Should be False"
    assert bad_luck(13) == True, "13 Should be True"
    assert bad_luck(13.0) == True, "13.0 Should be True"

if __name__ == "__main__":
    test()
    print("Everything passed. Ejercicio superado")