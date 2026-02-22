import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = input("\nEnter your guess: ")

        if not guess.isdigit():
            print("Please enter a valid number!")
            continue

        guess = int(guess)
        attempts += 1

        if guess < number:
            print("Too low! Try higher.")
        elif guess > number:
            print("Too high! Try lower.")
        else:
            print(f"Correct! You got it in {attempts} attempts!")
            break

    play_again = input("\nPlay again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()

play_game()









