students = []


def add_student(students):
    num = int(input("(How many students record would you like to add?): "))
    for i in range(num):
        name = input("Enter Name: ")
        age = int(input("Enter age: "))
        grades = float(input("Enter Grades: "))

        student = {
            "name": name,
            "age": age,
            "grades": grades
        }

        students.append(student)


def view_students(students):
    count = 1
    for student in students:
        print(
            f"{count}. {student['name']} - {student['age']} - {student['grades']}")
        count += 1


while True:
    print("--- Student Record Management ---")
    print("1. Add Student Record.")
    print("2. View All Students Record.")
    print("0. Exit System.")

    choice = int(input("Enter Number(0 - 5): "))

    match choice:
        case 1:
            add_student(students)

        case 2:
            view_students(students)

        case 0:
            break

        case _:
            print(":(Invalid Number... Try Again!)")
