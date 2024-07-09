num_sec = 2
adivinado = False

while not adivinado:
    num1 = int(input("Introduce el primer número: "))
    if num_sec == num1:
        print('Adivinaste')
        adivinado = True
    else:
        print('Ingresa de nuevo un número')
