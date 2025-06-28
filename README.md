# 🎲 Number Guessing Game

A fun and simple Python console game where you try to guess the number the computer is thinking of. Choose a difficulty level and test your guessing skills!

---

## 🚀 Features

- Difficulty levels: Easy, Medium, Hard
- Random number between 1 and 100
- Tracks number of attempts
- Replay option

---

## 🗂️ Project Structure

```
number_guessing_game/
├── main.py           # Entry point
├── game.py           # Core game logic
├── difficulty.py     # Difficulty levels using Enum
├── utils.py          # Helper functions (input validation)
└── README.md         # Project documentation
```

---

## ▶️ How to Run

1. Clone or download the repository:

```bash
git clone https://github.com/your-username/number-guessing-game.git
cd number-guessing-game
```

2. Run the game:

```bash
python main.py
```

---

## 📷 Example Output

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 67
Congratulations! You guessed the correct number in 2 attempts.
```
