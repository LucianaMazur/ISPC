"""Escribe un programa que solicite tres lados de un triángulo e
indique si es equilátero, isósceles o escaleno."""

lado1 = float(input("Ingrese un valor para el primer lado del triangulo: "))
lado2 = float(input("Ingrese un valor para el segundo lado del triangulo: "))
lado3 = float(input("Ingrese un valor para el tercer lado del triangulo: "))

if lado1 == lado2 and lado1 == lado3:
    print("Es un triangulo equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Es un triangulo isosceles")
else: 
    print("Es un triangulo escaleno")