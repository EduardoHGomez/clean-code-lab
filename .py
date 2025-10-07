import random  # Importa la librerí random

def startGame():
    number = random.randint(1, 20)  # Genera el nuemero entre 1 y 20
    guess = 0                       # Mantine el intento
    attempts = 0                    # Contador de intentos
    print("Adivina el número entre 1 y 20")  # Mensaje incio 

    # Mientras el numero no se adivine
    while guess != number:
        try:
            guess = int(input("Ingresa tu intento: "))  # Pide al usuario un número
            attempts += 1                               # Suma un intento

            if guess < number:
                print("Muy bajo")   # Si el numero es menor al correcto
            elif guess > number:
                print("Muy alto")   # Si el numero es mayor al correcto
            else:
                print("¡Correcto!")  # Si adivina
                print("Número de intentos:", attempts)
        except ValueError:
            # Si el usuario mete datos que no van 
            print("Error: debes ingresar un número válido.")

# Tira funcion
startGame()
