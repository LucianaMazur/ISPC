"""Escribe un programa que pida al usuario los dos catetos de un
triángulo rectángulo y calcule la hipotenusa."""
import math
cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print("La hipotenusa del triangulo es: ", hipotenusa)
