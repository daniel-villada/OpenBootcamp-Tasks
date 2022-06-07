#En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo,
# haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.

from pickle import *

class Vehiculo:

    def __init__(self, marca, color, ruedas):
        self.marca = marca
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Marca: {self.marca}\n' \
               f'Color: {self.color}\n' \
               f'Ruedas: {self.ruedas}'


coche = Vehiculo("BMW", "Negro", 4)
print(coche)

file = open('coche', 'w+b')
dump(coche, file)

file.seek(0)
coche = load(file)

print(coche)
file.close()