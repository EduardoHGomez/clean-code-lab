def getInputNumber():
    while True:
        s = input("Ingresa el numero: ")
        # Validat input que sea correcto
        try:
            return int(s)
        except ValueError:
            print("Ingresa un numero, intenta de nuevo")  

def validateGuess(guess: int):
    result = False
    if guess < number:
        print("Muy bajo")
    elif guess > number:
        print("Muy alto")
    elif guess == number:
        print("¡Correcto!")
        result = True
    return result

def startGame():
    number = random.randint(1, 20)
    guess = 0
    attempts = 0
    print("Adivina el número entre 1 y 20")
    while guess != number:
        userNumber = getInputNumber()
        attempts += 1
        result = validateGuess(userNumber)
        print("Número de intentos:", attempts)
        if result:
            return
        

# DMain the python
if __name__ == "__main__":
    print("Starting game...")
    startGame()
  
