# -*- coding: utf-8 -*-

# Dispones de una lista de participantes en un concurso, cada participante es una lista con 5 elementos:
# el numero de dorsal
# el nombre del participante
# el tiempo que hizo en la 1ª prueba
# el tiempo que hizo en la 2ª prueba
# el tiempo que hizo en la 3ª prueba

# Crea una función llamada disqualification que reciba una lista de participantes y un tiempo mínimo,
# y devuelva una lista con los nombres de los participantes que su tiempo medio sea menor que el tiempo mínimo
# El ejercicio para estar 100% correcto debe usar list comprehension o funciones lambda o funcinoes de orden superior
# Si se usan bucles tradiconales for o while el ejercicio valdrá la mitad.
# Lo ideal es hacer el ejercicio en una sola instrucción (línea de código)
# Los test deberán pasar correctamente.
# Cuidado con los decimales


def disqualification(products, min):
    #pon aqui tu codigo
    pass

participantes = [
  [ 4, 'jose', 20.3, 23.5, 44.2 ],
  [ 5, 'ruben', 23, 23.7, 44.4 ],
  [ 2, 'antia', 23.3, 23.5, 43.2 ],
  [ 11, 'susana', 35.3, 23.9, 41.3 ],
  [ 35, 'pedro', 3.3, 20.3, 37.2 ]
]

def test():
    assert disqualification(participantes,30)==['jose', 'pedro'],  "No se descalificó a los correctos"
    assert disqualification(participantes,23)==['pedro'], "Pedro tendría que estar"
    assert disqualification([],20)==[], "Si no hay participantes, la lista devuelta debe estar vacía"
    assert disqualification(participantes,0)==[], "Si no minimo, la lista devuelta debe estar vacía"


if __name__ == "__main__":
    test()
    print("Everything passed")


