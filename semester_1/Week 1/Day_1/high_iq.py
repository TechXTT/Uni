while True:
    num = int(input("Enter a number below 10: "))

    if num < 10:
        if num == 9:
            print("You win!")
        else:
            print("I win!")
    else:
        print("Number must be lower than 10.")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "n":
        break