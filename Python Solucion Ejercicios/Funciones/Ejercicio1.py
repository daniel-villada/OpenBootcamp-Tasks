
#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros
# y otra función que calcule el área de un círculo recibiendo el radio del mismo.

def areaTriangulo(altura, base):
    return base * altura / 2

print(f"El area del triangulo es: {areaTriangulo(10,20)}")

def areaCirculo(diametro):
    radio =  diametro / 2
    pi = 3.14
    return pi * radio ** 2

print(f"El area del circulo es: {areaCirculo(38)}")
