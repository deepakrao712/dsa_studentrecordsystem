students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append({'roll': roll, 'name': name, 'marks': marks})
    print(" Student added successfully.\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return
    print(" Student Records:")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    found = False
    for s in students:
        if s['roll'] == roll:
            print(f" Found: Roll: {s['roll']}, Name: {s['name']}, Marks: {s['marks']}\n")
            found = True
            break
    if not found:
        print(" Student not found.\n")

def update_marks():
    roll = input("Enter Roll Number to Update Marks: ")
    for s in students:
        if s['roll'] == roll:
            new_marks = float(input("Enter New Marks: "))
            s['marks'] = new_marks
            print(" Marks updated.\n")
            return
    print(" Student not found.\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for i in range(len(students)):
        if students[i]['roll'] == roll:
            del students[i]
            print("Student record deleted.\n")
            return
    print(" Student not found.\n")

def sort_by_marks():
    students.sort(key=lambda x: x['marks'], reverse=True)
    print(" Students sorted by marks (highest to lowest).\n")

def menu():
    while True:
        print("=== Student Record System ===")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll No")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Sort by Marks")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_marks()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            sort_by_marks()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("️ Invalid choice. Try again.\n")

menu()
