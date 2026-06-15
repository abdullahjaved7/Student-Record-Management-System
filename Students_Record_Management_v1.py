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

        print("Student record added successfully!")


def view_students(students):

    count = 1
    print("  | Name    | Age | Grades |")
    for student in students:
        print(
            f"{count}. {student['name']} - {student['age']} - {student['grades']}")
        count += 1


def search_student(students):
    s_name = input("Enter Student Name: ")
    for s in students:
        if s["name"] == s_name:
            print("STUDENT RECORD:")
            print(f" {s['name']} - {s['age']} - {s['grades']}")
            break
        else:
            print("Student Record Not Found.")


while True:
    print("--- Student Record Management ---")
    print("1. Add Student Record.")
    print("2. View All Students Record.")
    print("3. Search for a Student record.")
    print("0. Exit System.")

    choice = int(input("Enter Number(0 - 5): "))

    match choice:
        case 1:
            add_student(students)

        case 2:
            view_students(students)

        case 3:
            search_student(students)

        case 0:
            break

        case _:
            print(":(Invalid Number... Try Again!)")
