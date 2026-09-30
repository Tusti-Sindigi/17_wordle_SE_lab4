import random
from words import WORDS
from feedback import evaluate


class WordleGame:
    MAX_GUESSES = 6

    def __init__(self, length=5):
        self.length = length
        pool = [w for w in WORDS if len(w) == length]
        if not pool:
            raise ValueError(f"No {length}-letter words in words.py")
        self.target = random.choice(pool)
        self.history = []

    def show_history(self):
        print("History:")
        if not self.history:
            print("  (no guesses yet)")
        for n, (word, fb) in enumerate(self.history, 1):
            print(f"  {n}. {word}  {' '.join(fb)}")

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