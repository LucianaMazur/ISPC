"""Escribe un programa que solicite al usuario que ingrese una
contraseña y confirme la contraseña. El programa debe verificar si
ambas contraseñas coinciden y no están vacías."""

contrasenia = input("Ingrese su contraseña: ")
confirmacion = input("Confirme su contraseña: ")

if contrasenia == confirmacion and contrasenia != "" :
    print("CONTRASEÑA CONFIRMADA")
elif contrasenia != confirmacion:
    if contrasenia == "" or confirmacion == "":
        print("Debe llenar todos los campos requeridos")
    else: print("Las contraseñas no coinciden")