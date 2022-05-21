def es_primo():
    num = int(input("ingrese un numero: "))
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True

es_primo()