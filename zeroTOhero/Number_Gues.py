import random

from pandas import pivot

print("Hi! Welcome to number guessing game. You have 7 chances to guess number. Let's Start!1")

low = int(input("Enter the lower bound: "))
high = int(input("Enter the higher bound: "))

print(f"You have 7 chances to guess the number between {low} and {high}. Let's Start.")

num = random.randint(low,high)
ch = 7
gc = 0

while gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    if guess == num:
        print(f"Correct The number is {guess}. You guessed it in {gc} attempts.")
        break
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")
    elif guess > num:
        print("Too high! Try a lower number.")
    elif guess < num:
        print("Too low! Try a higher number.")
