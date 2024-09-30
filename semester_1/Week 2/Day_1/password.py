password = "password"

user_password = ""
print("Welcome to the password checker!")
counter = 0
while user_password != password:
    user_password = input("Enter password: ")
    if user_password == password:
        print("Password correct!")
        break
    else:
        print("Password incorrect!")