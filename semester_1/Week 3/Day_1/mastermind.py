def generate_code():
    import random
    code = []
    for i in range(4):
        code.append(random.randint(1, 8))
    return code

def check_guess(code, guess):
    correct = 0
    misplaced = 0
    code_copy = code[:]
    guess_copy = guess[:]

    # First pass: count correct digits
    for i in range(len(code)):
        if code[i] == guess[i]:
            correct += 1
            code_copy[i] = guess_copy[i] = None

    # Second pass: count misplaced digits
    for i in range(len(code)):
        if guess_copy[i] is not None and guess_copy[i] in code_copy:
            misplaced += 1
            code_copy[code_copy.index(guess_copy[i])] = None

    return correct, misplaced


def main():
    code = generate_code()
    print("Welcome to Mastermind!")
    print("The code has been generated.")
    print("The code is a 4 digit number.")
    print("The digits range from 1 to 8.")
    print("You have 10 guesses.")
    print("Good luck!")
    guesses = 0
    while guesses < 10:
        guess = input("Enter your guess: ")
        guess = [int(x) for x in guess]
        if len(guess) != 4:
            print("Invalid guess. Please enter a 4 digit number.")
            continue
        correct, misplaced = check_guess(code, guess)
        print(f"Correct: {correct}, Misplaced: {misplaced}")
        if correct == 4:
            print("Congratulations! You have guessed the code!")
            break
        guesses += 1
    if guesses == 10:
        print("You have run out of guesses. The code was:")
        print(code)

if __name__ == "__main__":
    main()