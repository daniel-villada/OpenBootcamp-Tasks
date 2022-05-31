

class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0


bmw = Coche()
bmw.color = 'Black'
bmw.ruedas = 4
bmw.puertas = 4
bmw.velocidad = 150
bmw.cilindrada = 1200

print(f'Color del coche: {bmw.color}\nNo. Ruedas: {bmw.ruedas}\nNo. Puertas: {bmw.puertas}\nVelocidad: {bmw.velocidad}\nCilindrada: {bmw.cilindrada}')