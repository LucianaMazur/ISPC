"""Escribe un programa que permita realizar la división de dos
números siempre y cuando el denominador no sea 0."""

dividendo = int(input("Ingrese un dividendo "))
divisor = int(input("Ingrese un divisor "))

if divisor != 0:
    print("El resultado de la division es:", dividendo/divisor)
else:
    print("No se puede realizar la division")