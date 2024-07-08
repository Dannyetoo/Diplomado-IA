while True:
    try:

        edad = int(input("Ingresa la edad: "))

        if 0 <= edad < 13:
            print("Categoría: Niño")
        elif 13 <= edad < 18:
            print("Categoría: Adolescente")
        elif 18 <= edad < 65:
            print("Categoría: Adulto")
        elif 65 <= edad < 150:
            print("Edad inválida, Ingresa una edad entre 0 y 150.")
            continue #Iniciar bucle si la edad es inválida
        break #Salir del bucle si la edad es válida
    except ValueError:
        print("Entrada inválida, ingrese otro número")
