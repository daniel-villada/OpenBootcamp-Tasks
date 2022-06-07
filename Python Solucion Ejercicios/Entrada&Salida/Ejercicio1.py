#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

file = open('file.txt', 'w')
file.write("Creando archivo txt desde python\n")
file.close()

file = open('file.txt', 'r+')
file.readline()
file.write('Que genial es esto.\n')
print(file.read())
file.close()