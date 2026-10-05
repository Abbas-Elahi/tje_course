import random

secret_number = random.randint(1, 20)
while True:
    guess = int(input("Guess: "))
    if guess < secret_number:
        print("📈 Go higher!")
    elif guess > secret_number:
        print("📉 Go lower!")
    else:
        print("🎉 YOU WIN!")
        break
