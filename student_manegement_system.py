students = []

def read_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("\n Input cannot be empty.")

def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None

def read_int(prompt, minimum=None):
    while True:
        try:
            value = int(input(prompt).strip())
        except ValueError:
            print("\n Please enter a whole number.")
            continue
        if minimum is not None and value < minimum:
            print(f"\n Number must be at least {minimum}.")
        else:
            return value

def read_marks(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("\n Please enter a valid number.")
            continue
        if 0 <= value <= 100:
            return value
        print("\n Marks must be between 0 and 100.")         

def get_grade(marks):
    if marks >= 75:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 55:
        return "C"
    elif marks >= 40:
        return "S"
    else:
        return "F"


      
def add_student():
    print("\n--- Add Student ---")

    # Automatically generate student ID
    if len(students) == 0:
        student_id = 1
    else:
        student_id = max(student["id"] for student in students) + 1

    print(f"Automatically generated Student ID: {student_id}")

    name = read_text("Enter student name: ")
    marks = read_marks("Enter marks (0-100): ")

    student = {
        "id": student_id,
        "name": name,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")
    print(f"Student ID: {student_id}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {get_grade(marks)}")

def view_all_students():
    print("\n--- All Students ---")
    if len(students) == 0:
        print("\n No students found.")
        return

    print("\nID\tName\t\tMarks\tGrade")
    print("-" * 50)
    for student in students:
        print(student["id"], "\t", student["name"], "\t\t",
              student["marks"], "\t", get_grade(student["marks"]))


def search_student():
    print("\n--- Search Student by ID ---")
    student_id = read_int("Enter student ID to search: " , minimum=1)
    student = find_student(student_id)

    if student is None:
        print("\n Student not found.")
    else:
        print("\nID:", student["id"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Grade:", get_grade(student["marks"]))


def update_marks():
    print("\n--- Update Student Marks ---")
    student_id = read_int("Enter student ID: " , minimum=1)
    student = find_student(student_id)

    if student is None:
        print("Student not found.")
        return
    print(f"Student: {student['name']} | Current marks: {student['marks']}")
    new_marks = read_marks("Enter new marks (0-100): ")

    if new_marks < 0 or new_marks > 100:
        print("Marks must be between 0 and 100!")
        return

    student["marks"] = new_marks
    print("\n Marks updated successfully!")


def delete_student():
    print("\n--- Delete Student ---")
    if not students:
        print("No students found.")
        return
    
    student_id = read_int("Enter student ID to delete: " , minimum=1)
    student = find_student(student_id)

    if student is None:
       print("Student not found.")
       return
    confirm = input(
           f"Are you sure you want to delete {student['name']}? (y/n): ")

    if confirm.strip().lower() == "y":
            
            students.remove(student)
            print("\n Student deleted successfully!")
    else:
         print("Deletion cancelled.")

def grade_report():
    print("\n----- Grade Report -----")

    if len(students) == 0:
        print("No students found.")
        return
    ranked = sorted(students, key=lambda s: s["marks"], reverse=True)
    print(f"{'Rank':<6}{'ID':<8}{'Name':<22}{'Marks':<9}{'Grade':<6}")
    print("-" * 51)
    for rank, s in enumerate(ranked, start=1):
        print(
    f"{rank:<6}{s['id']:<8}{s['name']:<22}"
    f"{s['marks']:<9.1f}{get_grade(s['marks']):<6}"
)
       
    print("-" * 51)

    all_marks = [s["marks"] for s in ranked]
    passed = sum(1 for m in all_marks if m >= 40)
    print(f"Class average : {sum(all_marks) / len(all_marks):.2f}")
    print(f"Highest marks : {ranked[0]['marks']:.1f} ({ranked[0]['name']})")
    print(f"Lowest marks  : {ranked[-1]['marks']:.1f} ({ranked[-1]['name']})")
    print(f"Passed        : {passed}/{len(ranked)}")

    print("\nGrade distribution:")
    for grade in ["A", "B", "C", "S", "F"]:
            count = sum(1 for s in ranked if get_grade(s["marks"]) == grade)
            print(f"  {grade}:  ({count})\n\n")
    
   
    print("\nTotal students:", len(students))
    

# ----- Main program -----
while True:
    print("=" * 100)
    print("STUDENT MANAGEMENT SYSTEM".center(100))
    print("=" * 100)
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student by ID")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Display Grade Report")
    print("7. Exit Application")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_marks()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        grade_report()
    elif choice == "7":
        print("Thank you for using the system !")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 7.")
