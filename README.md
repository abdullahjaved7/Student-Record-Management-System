# Student Record System

A console-based Student Record Management System built with Python.

This project allows users to manage student records through an interactive menu-driven interface. Users can add, view, search, update, and delete student records. All data is automatically saved and loaded between program sessions.

## Features

### Student Management

* Add student records
* View all student records
* Search students by ID
* Update student records
* Delete student records
* Display the top-performing student
* Calculate average grades

### Unique Student IDs

* Automatically generates a unique ID for each student
* Search, update, and delete operations use IDs for accurate record management

### Data Persistence

* Save student records to a file
* Automatically load records when the application starts
* Maintain data between program sessions

### Input Validation

* Integer input validation using `try/except`
* Float input validation using `try/except`
* Grade validation (0–100 range)

### Error Handling

* Handles missing data files gracefully
* Prevents operations on empty student records
* Prevents invalid numeric input

## Technologies Used

* Python
* Functions
* Lists
* Dictionaries
* Loops
* Match Case Statements
* File Handling
* Exception Handling
* Git
* GitHub

## Project Structure

```text
Student_Record_System/
│
├── main.py
├── record.txt
├── README.md
├── .gitignore
```

## Requirements

* Python 3.10 or higher

## Installation

### Clone the Repository

```bash
git clone <repository-url>
```

### Navigate to the Project Folder

```bash
cd Student_Record_System
```

### Run the Application

```bash
python main.py
```

## Example Menu

```text
--- Student Record Management ---

1. Add Student Record
2. View All Student Records
3. Search Student Record
4. Show Top Student
5. Show Average Grades
6. Delete Student Record
7. Update Student Record
0. Exit System
```

## Version History

### v0.1.0

* Add student records
* View student records
* Search student records
* Calculate average grades
* Display top student

### v0.2.0

* Added file persistence
* Added automatic record loading
* Improved empty record handling
* Improved top student calculation
* Data is now saved between sessions

### v0.3.0

* Added unique student IDs
* Added update student functionality
* Added delete student functionality
* Added input validation helpers
* Added grade validation (0–100)
* Updated search operations to use IDs
* Updated file storage to include student IDs
* Improved overall record management

## Roadmap

### v0.4.0

* Search by both Name and ID
* Save data using JSON
* Improve file handling with context managers (`with open`)
* Student statistics and reporting
* Code refactoring and optimization

### v0.5.0

* Graphical User Interface (GUI)
* Database integration
* Advanced student management features

## Learning Outcomes

This project helped me practice:

* Python Fundamentals
* Functions
* Lists and Dictionaries
* CRUD Operations (Create, Read, Update, Delete)
* File Handling
* Exception Handling
* Input Validation
* Problem Solving
* Git Workflow
* GitHub Workflow

## Author

**Abdullah Javed**

Aspiring Software Developer | AI Automation Engineer

Email: [eduabdullah7@gmail.com](mailto:eduabdullah7@gmail.com)
