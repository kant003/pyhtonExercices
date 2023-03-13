# -*- coding: utf-8 -*-

# Dispones de una lista de participantes en un concurso, cada participante es una lista con 5 elementos:
# el numero de dorsal
# el nombre del participante
# el tiempo que hizo en la 1ª prueba
# el tiempo que hizo en la 2ª prueba
# el tiempo que hizo en la 3ª prueba

# Guardar en un fichero la lista de participantes cuya media de sus 3 puntuaciones superan el tiempo mínimo (pasado como parametro)
# Guardar tambien en el mismo fichero el participante (o los participantes) que ha sacado el mejor tiempo medio
#   Nota: puede que varios participantes saquen el mismo tiempo medio mayor
# Cuidado con los decimales

# Ejemplo de salida de fichero:
            # Participantes que han superado el tiempo medio mínimo:
            # -Pedro
            # -Maria
            # -Luisa
            # Mejor o mejores participantes (tiempo medio):
            # -Pedro
            # -Luisa



fileOutput = "exam_recu/participantes.txt"

participants = [
    [1, "Juan", 10, 15, 20],
    [2, "Pedro", 12, 16, 18],
    [3, "Maria", 11, 14, 20.5],
    [4, "Luisa", 16, 12, 18],
    [5, "Ana", 9, 13, 21],
    [6, "Brais", 2, 12, 24]
]

def save(participants, min, fileOutput):
    #pon aqui tu codigo
    pass

save(participants,15.1,fileOutput)

def test():
    f = open(fileOutput, 'r')
    data = f.readlines()
    assert len(data)>0, "fichero vacio"
    f.close()

if __name__ == "__main__":
    test()
    print("Everything passed")


