def average(num_list: list) -> float:
    return sum(num_list) / len(num_list)

def average_segment(num_list: list, start: int, end: int) -> float:
    return average(num_list[start:end])

def input_numbers() -> list:
    num_list = []
    while True:
        number = input("Enter a number: ")
        if number == "":
            break
        num_list.append(float(number))
    return num_list

numbers = input_numbers()
if len(numbers) == 0:
    print("No numbers entered.")
else:
    for start in range(0, len(numbers), 7):
        print(f"Average for week {start // 7 + 1}: {average_segment(numbers, start, start + 7)}")
    
    for start in range(0, len(numbers), 30):
        print(f"Average for month {start // 30 + 1}: {average_segment(numbers, start, start + 30)}")
