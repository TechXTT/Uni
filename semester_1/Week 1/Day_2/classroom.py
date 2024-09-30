print("Hello to the classroom!")
subjects = {
    "Math": 401,
    "Science": 402,
    "History": 403,
    "English": 404
}
while True:
    student = input("Enter student name: ")
    subject = input("Enter student subject: ")
    if subject not in subjects:
        print("I don't know that subject.")
        continue
    
    print(f"Hi {student}, go to room {subjects[subject]}.")