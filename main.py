from game import WordleGame


def choose_length():
    while True:
        choice = input("Choose word length (4, 5 or 6): ").strip()
        if choice in ("4", "5", "6"):
            return int(choice)
        print("Please enter 4, 5 or 6.")


if __name__ == "__main__":
    WordleGame(choose_length()).run()