"""Encontrar el mayor de 3 números."""

numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese un numero: "))
numero3 = float(input("Ingrese un numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("El mayor de los tres numeros es: ", numero1)
elif numero2 > numero1 and numero2 > numero3:
    print("El mayor de los tres numeros es: ", numero2)
else:
    print("El mayor de los numeros es: ", numero3)