"""Escribe un programa que solicite al usuario el precio y la cantidad
de un producto. Clasifique el producto como "caro" si el precio es
mayor de $100 o si la cantidad es menor que 10 y el precio es
mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye
condiciones para manejar valores falsos (0 o vacío)."""

precio = float(input("Ingrese el precio del producto: "))
cantidad = float(input("Ingrese la cantidad de producto: "))


if precio == 0 or cantidad == 0:
    print("Error: El precio y la cantidad deben ser mayores que 0.")
else:
    
    if precio > 100 or (precio > 50 and cantidad < 10):
        print("El producto es caro.")
    else:
        print("El producto es barato.")