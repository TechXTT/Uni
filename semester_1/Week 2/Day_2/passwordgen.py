import random

length = random.randint(8, 12)

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
characters = ascii_letters + digits
password = ""
for _ in range(length):
    password += random.choice(characters)

print(password)
