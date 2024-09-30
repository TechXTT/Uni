import random

lord_of_the_strings = ["Frodo", "Sam", "Merry", "Pippin", "Aragorn", "Legolas", "Gimli", "Boromir", "Gandalf", "Sauron"]

print(random.choice(lord_of_the_strings))

rand_index = random.randint(0, len(lord_of_the_strings) - 1)

print(lord_of_the_strings[rand_index])