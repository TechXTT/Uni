names = []
heights = []

for i in range(3):
    name = input("Enter name: ")
    height = int(input("Enter height: "))
    names.append(name)
    heights.append(height)

tallest = max(heights)
tallest_index = heights.index(tallest)
tallest_name = names[tallest_index]

print(f"The tallest person is {tallest_name} at {tallest}cm.")