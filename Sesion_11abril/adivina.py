#Adivinar un número
import random

numero_secreto = random.randint(1,10)

while(True):
    numero_usuario = int(input("Dígame un número del 1 al 10: "))

    if(numero_secreto == numero_usuario):
        print(f"Felicidades, adivinaste el número secreto: {numero_secreto}")
        break
    else:
        print("Sigue intentando")
        
    if(numero_usuario > numero_secreto):
        print("El numero es menor")
    else:
        print("El numero es mayor")