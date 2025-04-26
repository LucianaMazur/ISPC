"""Escribe un programa que pida al usuario su año de nacimiento,
calcule su edad y genere un mensaje de saludo personalizado
que incluya su nombre y la edad calculada."""

nombre = input("Ingrese su nombre: ")
anioNacimiento = int(input("Ingrese el año de su naciemiento: "))
edad = 2025 - anioNacimiento
print("Hola ", nombre, "tu edad es: ", edad, "años!")