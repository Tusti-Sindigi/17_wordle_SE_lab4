import os
import random
from words import WORDS
from feedback import evaluate

os.system("")  # enables ANSI colour codes in the Windows console


class WordleGame:
    MAX_GUESSES = 6
    KEY_ROWS = ("ABCDEFGHIJKLM", "NOPQRSTUVWXYZ")
    RESET = "\033[0m"
    STYLES = {
        "green":  "\033[48;5;71m\033[38;5;16m\033[1m",
        "yellow": "\033[48;5;178m\033[38;5;16m\033[1m",
        "gray":   "\033[48;5;240m\033[38;5;231m\033[1m",
    }
    RANK = {"gray": 1, "yellow": 2, "green": 3}

    def __init__(self, length=5):
        self.length = length
        pool = [w for w in WORDS if len(w) == length]
        if not pool:
            raise ValueError(f"No {length}-letter words in words.py")
        self.target = random.choice(pool)
        self.history = []

    def letter_status(self):
        best = {}
        for word, fb in self.history:
            for ch, colour in zip(word, fb):
                if self.RANK[colour] > self.RANK.get(best.get(ch), 0):
                    best[ch] = colour
        return best

    def show_keyboard(self):
        if not self.history:
            return
        status = self.letter_status()
        print("Letters:")
        for row in self.KEY_ROWS:
            cells = []
            for ch in row:
                colour = status.get(ch.lower())
                if colour:
                    cells.append(f"{self.STYLES[colour]} {ch} {self.RESET}")
                else:
                    cells.append(f" {ch} ")
            print("  " + " ".join(cells))

    def show_history(self):
        print("History:")
        if not self.history:
            print("  (no guesses yet)")
        for n, (word, fb) in enumerate(self.history, 1):
            print(f"  {n}. {word}  {' '.join(fb)}")
        self.show_keyboard()

    def show_summary(self, outcome):
        print("\n=== Session summary ===")
        print(f"Result : {outcome}")
        print(f"Word   : {self.target}")
        print(f"Length : {self.length} letters")
        print(f"Guesses: {len(self.history)}/{self.MAX_GUESSES}")
        self.show_history()

    def run(self):
        print(f"Wordle — {self.length} letters, {self.MAX_GUESSES} guesses.")
        while len(self.history) < self.MAX_GUESSES:
            guess = input("> ").strip().lower()
            if guess == "q":
                print("Game quit. The word was:", self.target)
                self.show_summary("Quit")
                return
            if len(guess) != self.length or not guess.isalpha():
                print("Enter a valid word of the required length.")
                continue
            feedback = evaluate(self.target, guess)
            self.history.append((guess, feedback))
            print(" ".join(feedback))
            if guess == self.target:
                print(f"You win! Solved in {len(self.history)}/{self.MAX_GUESSES} guesses.")
                self.show_summary("Win")
                return
            if len(self.history) < self.MAX_GUESSES:
                self.show_history()
        print(f"You lose! The word was: {self.target}")
        self.show_summary("Loss")