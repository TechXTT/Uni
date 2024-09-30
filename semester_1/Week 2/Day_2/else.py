import random

dice = [random.randint(1, 6) for _ in range(2)]

print(f"Rolls: {dice} Sum: {sum(dice)}")