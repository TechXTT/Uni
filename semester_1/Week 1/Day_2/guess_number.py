print("Guess the number!")
import random

games = []

number = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    guess = input("Enter a number between 1 and 100: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    elif int(guess) < 1 or int(guess) > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if guess == number:
        print("You guessed the number! It took you", counter, "tries.")
        games.append(counter)
        games.sort()
        again = input("Do you want to play again? (y/n) ")
        if again == "n":
            break
        else:
            number = random.randint(1, 100)
            counter = 0
    elif guess < number:
        print("Number is higher.")
    else:
        print("Number is lower.")

print("Your best score is", games[0], "tries.")