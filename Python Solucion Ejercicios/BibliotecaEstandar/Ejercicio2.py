#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
# parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.


from functools import reduce

def getImpares(lista):
    result = list(filter((lambda x: x % 2), listNumbers))
    print(result)

    result = reduce((lambda x, y: x + y), result)
    print(result)

listNumbers = list(range(100))

getImpares(list)