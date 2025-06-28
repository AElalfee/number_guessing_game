from enum import Enum


class Difficulty(Enum):
    EASY = (1, 10, "Easy")
    MEDIUM = (2, 5, "Medium")
    HARD = (3, 3, "Hard")

    def __init__(self, code, chances, mode):
        self.code = code
        self.chances = chances
        self.mode = mode

    @staticmethod
    def user_choice(choice):
        for level in Difficulty:
            if level.code == choice:
                return level.chances
        return None
