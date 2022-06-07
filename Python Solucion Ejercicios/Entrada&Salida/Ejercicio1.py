#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt,
# lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

file = open('file.txt', 'w')
file.write("Creando archivo txt desde python\n")
file.write("que genial...\n")
file.close()