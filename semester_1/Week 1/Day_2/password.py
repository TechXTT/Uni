password = "password"

print("Welcome to the password checker!")
counter = 0
while counter < 3:
    user_password = input("Enter password: ")
    if user_password == password:
        print("Password correct!")
        break
    else:
        print("Password incorrect!")
        counter += 1
        if counter == 3:
            print("Your account has been blocked.")
            break
        print(f"You have {3-counter} tries left.")