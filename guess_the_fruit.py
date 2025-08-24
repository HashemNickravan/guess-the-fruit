"""A simple fruit guessing game where the player must guess the hidden fruit."""

import random


def play_guess_the_fruit():
    """Run the fruit guessing game."""
    fruits = [
        "apple",
        "banana",
        "cherry",
        "apricot",
        "grape",
        "watermelon",
        "mango",
        "orange",
        "peach",
        "pineapple",
        "melon",
        "kiwi",
        "plum",
        "lemon",
        "avocado",
        "fig",
    ]
    fruit = random.choice(fruits).lower()
    guessed = ["_"] * len(fruit)
    chances = len(fruit)
    used_letters = set()

    print("Guess the fruit Game")
    print(f"The fruit has been chosen. You have {chances} chances.")
    print(" ".join(guessed))
    print("\n")

    while chances > 0 and "_" in guessed:
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        if guess in used_letters:
            print("You have already tried this letter.")
            continue

        used_letters.add(guess)

        if guess in fruit:
            for index, letter in enumerate(fruit):
                if letter == guess:
                    guessed[index] = guess
            print("Correct guess!")
        else:
            chances -= 1
            print(f"Wrong guess. Chances left: {chances}")

        print(" ".join(guessed))

    if "_" not in guessed:
        print(f"Congratulations! You guessed the fruit: {fruit}")
    else:
        print(f"Game over. The fruit was: {fruit}")


if __name__ == "__main__":
    play_guess_the_fruit()
