n = int(input("Num of people: "))

toppings = []
while(1):
    topping = input("Enter topping: ")
    if topping == "done":
        break
    toppings.append(topping)
    
egg_types = []
while(1):
    egg_type = input("Enter egg type: ")
    if egg_type == "done":
        break
    egg_types.append(egg_type)

for i in range(n):
    print ("Person", i+1, "choose from the following toppings: ")
    for j in range(len(toppings)):
        print (j+1, toppings[j])
    topping_choice = input("Enter choice: ")
    if "," in topping_choice:
        topping_choice = topping_choice.split(",")
        for j in range(len(topping_choice)):
            topping_choice[j] = int(topping_choice[j])
    else:
        topping_choice = int

    print ("Person", i+1, "choose from the following egg types: ")
    for j in range(len(egg_types)):
        print (j+1, egg_types[j])
    egg_type_choice = int(input("Enter choice: "))

    print ("Person", i+1, "choose a number of eggs: ")
    num_eggs = int(input("Enter choice: "))

    print ("Person", i+1, "chose the following toppings: ")
    for j in range(len(topping_choice)):
        print (toppings[topping_choice[j]-1])
    print ("Person", i+1, "chose ", num_eggs, " of ", egg_types[egg_type_choice-1], "eggs")
    print ("---------------------------------")

