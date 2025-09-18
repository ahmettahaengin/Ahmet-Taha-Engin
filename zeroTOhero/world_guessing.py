import random

from zeroTOhero.Number_Gues import guess

name = input("What's your name ? ")

print(f"Welcome to my game good luck {name}.")

words = [
    'rainbow', 'computer', 'science', 'programming',
    'python', 'mathematics', 'player', 'condition',
    'reverse', 'water', 'board', 'geeks'
]

word = random.choice(words)

print("Guess the characters.")

guesses = ""

turns = len(words)

while turns > 0:

    failed = 0

    for char in word:

        if char in guesses:
            print(char, end="")

        else:
            print("_")
            failed += 1

    if failed == 0:
        print(f"You Win. The word is {word}")
        break

    print()
    guess = input("guess a character: ")

    guesses += guess

    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, "more guesses ")

        if turns == 0:
            print("You loose")
            



