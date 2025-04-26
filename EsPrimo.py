"""Escribe un programa que a partir de un número entero positivo,
muestre por pantalla si es primo o no."""

numero = int(input("Ingrese un número entero positivo: "))

if numero < 2:
    print("El número no es primo")
else:
    esPrimo = True 

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            esPrimo = False
            break

    if esPrimo:
        print("El número es primo")
    else:
        print("El número no es primo")