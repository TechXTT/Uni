import random

def print_hangman(tries):
    if tries == 6:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif tries == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========")
    elif tries == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========")
    elif tries == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========")
    elif tries == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print("      |")
        print("      |")
        print("=========")
    elif tries == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" /    |")
        print("      |")
        print("=========")
    elif tries == 0:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\\  |")
        print(" / \\  |")
        print("      |")
        print("=========")

def print_word(word, guesses):
    for letter in word:
        if letter in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def main():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "watermelon"]
    word = random.choice(words)
    guesses = []
    tries = 6
    print("Welcome to Hangman!")
    print("The word has been chosen.")
    print("The word is a fruit.")
    print("You have 6 tries.")
    print("Good luck!")
    while tries > 0:
        print_hangman(tries)
        print_word(word, guesses)
        guess = input("Enter your guess: ")
        if len(guess) != 1:
            print("Invalid guess. Please enter a single letter.")
            continue
        if guess in guesses:
            print("You have already guessed that letter.")
            continue
        guesses.append(guess)
        if guess not in word:
            tries -= 1
        if all(letter in guesses for letter in word):
            print_word(word, guesses)
            print("Congratulations! You have guessed the word!")
            break
    if tries == 0:
        print_hangman(tries)
        print("You have run out of tries. The word was:")
        print(word)

if __name__ == "__main__":
    main()