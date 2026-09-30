from collections import Counter


def evaluate(target, guess):
    # Two-pass scoring so each target letter is only "used" once:
    #   Pass 1: mark greens, and count the target letters NOT matched by a green.
    #   Pass 2: mark yellows left to right, only while unmatched copies remain.
    result = ["gray"] * len(guess)
    remaining = Counter()

    for i, ch in enumerate(guess):
        if ch == target[i]:
            result[i] = "green"
        else:
            remaining[target[i]] += 1

    for i, ch in enumerate(guess):
        if result[i] == "green":
            continue
        if remaining[ch] > 0:
            result[i] = "yellow"
            remaining[ch] -= 1

    return result