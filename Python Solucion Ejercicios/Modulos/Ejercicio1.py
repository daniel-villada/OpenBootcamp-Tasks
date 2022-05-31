#importando modulo operaciones

from Operaciones import *

num1, num2, num3, num4 = (3, 6, 10, 5)

print("{} + {} = {}".format(num1, num2, suma(num1, num2)))
print("{} - {} = {}".format(num3, num4, resta(num3, num4)))
print("{} * {} = {}".format(num4, num1, multiplicacion(num4, num1)))
print("{} / {} = {}".format(num3, num2, division(num3, num2)))


