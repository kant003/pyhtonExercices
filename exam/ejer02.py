# -*- coding: utf-8 -*-

# Hay un fichero llamado a.txt con las puntuaciones de un juego de los años 80. 
# Cada línea tiene el nombre del jugador y su puntuación separados por dos puntos.
# Una línea es válida si:
# - el nombre del jugador tiene 3 caracteres 
# - y la puntuación es un valor comprendido entre 0 y 10000 (incluidos)
# puede haber también líneas corruptas que no cumplan estas condiciones

# Tu tareas será:

# 1. Crear una función count_lines_corrupted(file), 
# que reciba el nombre del fichero y devuelva el número total de líneas corruptas o no válidas

# 2. Crear una función add_scores(file, user),
# que reciba el nombre del fichero y el nombre de un jugador, y devuelva la suma de todas las puntuaciones de ese jugador

# 3. Crear una función winner(file),
# que reciba el nombre del fichero y devuelva el nombre del jugador que más puntuación ha sacado

# 4. Crear una función def hall_of_fame(file),
# que reciba el nombre del fichero y devuelva una lista con los nombres de los 3 jugadores con más puntuación

# Nota1: No olvides que con los datos que tienes que trabajar son los que no están corruptos y que cumplan con los criterios dados
# Nota2: Tines un fichero de ejemplo a.txt en esta carpeta
# Nota3: Usa funciones para no repetir código innecesariamente y que todo sea más legible
# Nota4: Mientras haces el ejercicio puedes ir ocultando algunos los test para ir programando poco a poco

def count_lines_corrupted(file):
    # Tu código aquí


def add_scores(file, user):
    # Tu código aquí


def winner(file):
    # Tu código aquí


def hall_of_fame(file):
    # Tu código aquí







def test():
    assert count_lines_corrupted('exam/a.txt')==6, "Hay 6 lineas corruptas"
    assert add_scores('exam/a.txt','DGC')==791, "El score total de DGC es 791"
    assert add_scores('exam/a.txt','LUC')==979, "El score total de LUC es 979"
    assert add_scores('exam/a.txt','REC')==0, "El score total de REC es 0 (no existe)"
    assert add_scores('exam/a.txt',None)==0, "El score total de None es 0"
    assert winner('exam/a.txt')=='SIT', "El jugador con el mayor score es SIT"
    assert hall_of_fame('exam/a.txt')==['SIT', 'LUC', 'DGC'], "Los 3 jugadores con mejor puntuacion son SIT LUC Y DGC por orden"

if __name__ == "__main__":
    test()
    print("Everything passed. Ejercicio superado")