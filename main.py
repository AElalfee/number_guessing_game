from game import play
from difficulty import Difficulty


def main():
    while True:
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100.")

        while True:
            print("Please select the difficulty level:")

            for level in Difficulty:
                print(f"{level.code}. {level.mode} ({level.chances} chances)")

            choice = input("Enter your choice: ")
            difficulity = Difficulty.user_choice(int(choice))

            if difficulity:
                break
            else:
                print("Invalid choice. Please select a valid difficulty.\n")

        play(difficulity)

        replay = input("\nDo you want to play again? (yes/no): ").strip().lower()

        if replay not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
