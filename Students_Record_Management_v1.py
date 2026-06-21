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
    if not students:
        print("Student Record is Empty.")
        return

    count = 1
    print("  | Name    | Age | Grades |")
    for student in students:
        print(
            f"{count}. {student['name']} - {student['age']} - {student['grades']}")
        count += 1


def search_student(students):
    if not students:
        print("Student Record is Empty.")
        return
    s_name = input("Enter Student Name: ")
    found = False
    for s in students:
        if s["name"] == s_name:
            print("STUDENT RECORD:")
            print(f" {s['name']} - {s['age']} - {s['grades']}")
            found = True
            break

    if not found:
        print("Student Record Not Found.")


def top_student(students):
    if not students:
        print("Student Record is Empty.")
        return

    top = students[0]
    for student in students:
        if student["grades"] > top["grades"]:

            top = student

    print(f"{top['name']} - {top['age']} - {top['grades']}")


def average_grades(students):
    if not students:
        print("Student Record is Empty.")
        return

    grades_sum = 0
    count = 0
    for student in students:
        if student["grades"] >= 0:
            grades_sum += student["grades"]
            count += 1

    avg_grades = grades_sum / count
    print(f"Average grades: {avg_grades:.2f}")


def save_data(students):
    file = open("record.txt", "w")

    for student in students:
        line = f"{student['name']},{student['age']},{student['grades']}"
        file.write(line)
        file.write("\n")

    file.close()


def load_data(students):
    try:
        file = open("record.txt", "r")

        for line in file:
            line = line.strip()
            parts = line.split(",")
            student = {
                "name": parts[0],
                "age": int(parts[1]),
                "grades": float(parts[2])
            }
            students.append(student)
        print("File loaded successfully :)")
        file.close()
    except FileNotFoundError:
        print("No saved records found. Starting with an empty database.")


load_data(students)


while True:
    print("--- Student Record Management ---")
    print("1. Add Student Record.")
    print("2. View All Students Record.")
    print("3. Search for a Student record.")
    print("4. Show Top Student.")
    print("5. Show average grades.")
    print("0. Exit System.")

    choice = int(input("Enter Number(0 - 5): "))

    match choice:
        case 1:
            add_student(students)

        case 2:
            view_students(students)

        case 3:
            search_student(students)

        case 4:
            top_student(students)

        case 5:
            average_grades(students)

        case 0:
            save_data(students)
            break

        case _:
            print(":(Invalid Number... Try Again!)")
