#built a student record managment system using list, dictionaries, function,loop and condition

# Student Record Management System

students = []


# Add student
def add_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    age = int(input("Enter Age: "))
    marks = float(input("Enter Marks: "))

    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)
    print("Student added successfully!")


# Display students
def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records:")

        for student in students:
            print("----------------------")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Marks   :", student["marks"])


# Search student
def search_student():
    roll_no = int(input("Enter Roll Number to search: "))

    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("Roll No :", student["roll_no"])
            print("Name    :", student["name"])
            print("Age     :", student["age"])
            print("Marks   :", student["marks"])
            found = True
            break

    if found == False:
        print("Student not found.")


# Delete student
def delete_student():
    roll_no = int(input("Enter Roll Number to delete: "))

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


# Main menu
while True:
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.") 