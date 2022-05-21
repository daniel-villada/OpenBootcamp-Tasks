
#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# y otra función que calcule el área de un círculo recibiendo el radio del mismo.

import math

def areaTriangulo(altura, base):
    return ((base * altura) / 2)

print(f"El area del triangulo es: {areaTriangulo(10,20)}")

def areaCirculo(radio):
    return (math.pi * radio ** 2)

print(f"El area del circulo es: {areaCirculo(19)}")
