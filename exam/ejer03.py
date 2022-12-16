# -*- coding: utf-8 -*-

# Crea una función llamada exceed_cost que reciba una lista de productos y un coste máximo, 
# y devuelva una lista con los nombres de los productos que su precio final(precio*cantidad) superen un coste máximo
# Cada producto es una lista con 4 elementos: id, nombre, precio, cantidad
# El ejercicio para estar 100% correcto debe usar list comprehension o funciones lambda o funcinoes de orden superior
# Si se usan bucles tradiconales (for o while) el ejercicio valdrá la mitad.
# Lo ideal es hacer el ejercicio con una sola instrucción (línea de código)

def exceed_cost(products, max_cost):
    # tu código aquí


products = [
  [ 11, 'fresa', 20.3, 234 ],
  [ 2, 'pera', 23, 234 ],
  [ 12, 'lima', 23.3, 345 ],
  [ 9, 'limon', 35.3, 453 ],
  [ 3, 'naranja', 3.3, 345 ]
]

def test():
    assert exceed_cost(products,5000)==['pera', 'lima', 'limon'], "La pera, la lima y el limón superan el coste máximo"
    assert exceed_cost(products,0)==['fresa','pera', 'lima', 'limon', 'naranja'], "La pera, la lima y el limón superan el coste máximo"
    assert exceed_cost([],5000)==[], "Si no hay productos, la lista devuelta debe estar vacía"


if __name__ == "__main__":
    test()
    print("Everything passed. Ejercicio superado")

