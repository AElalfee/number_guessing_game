import random


def play(chances):
    number = random.randint(1, 100)
    attempts = 0

    while chances > 0:
        guess = input("Enter your guess: ")
        attempts += 1

        if int(guess) == number:
            print(
                f"Congratulations! You guessed the correct number in {attempts} attempts."
            )
            break
        elif int(guess) < number:
            print("Incorrect! The number is greater than", guess)
        else:
            print("Incorrect! The number is less than", guess)

        chances -= 1
    else:
        print(f"\n Game Over! The correct number was {number}.")
