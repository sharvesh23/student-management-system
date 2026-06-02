class Student:
    def __init__(self, Student_name, Student_rollno, Student_department, Phone_number):
        self.Student_name = Student_name
        self.Student_rollno = Student_rollno
        self.Student_department = Student_department
        self.Phone_number = Phone_number

    def display(self):
        print(f"Name: {self.Student_name}")
        print(f"Rollno: {self.Student_rollno}")
        print(f"Department: {self.Student_department}")
        print(f"Phone Number: {self.Phone_number}")

    def update(self, Student_name, Student_department, Phone_number):
        self.Student_name = Student_name
        self.Student_department = Student_department
        self.Phone_number = Phone_number
        
students = []

def add_student():
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll no: ")
    department = input("Enter Department:")
    contact_no = int(input("Enter Parents Number:"))

    for student in students:
        if student.Student_rollno == roll_2no:
            print("This roll no already exists")
            return
    new_student = Student(name, roll_no, department, contact_no)

    students.append(new_student)

def display_student():
    print("Student Details:")
    for student in students:
        student.display()

def search_student():
    roll_no = input("Enter Roll no to search: ")
    for student in students:
        if student.Student_rollno == roll_no:
            print("Student found:")
            student.display()
            return
        else:
            print("Student not found")

def update_student():
    roll_no = input("Enter Roll no to update: ")
    for student in students:
        if student.Student_rollno == roll_no:
            print("Student found:")
            name = input("Enter new Name: ")
            department = input("Enter new Department: ")
            contact_no = int(input("Enter new Parents Number: "))
            student.update(name, department, contact_no)
            print("Student updated successfully.")
            return
        else:
            print("Student not found")

def delete_student():
    roll_no = input("Enter Roll no to delete: ")
    for student in students:
        if student.Student_rollno == roll_no:
            students.remove(student)
            print("Student deleted successfully.")
            return
        else:
            print("Student not found")

while True:
    print("-------------------Student Management System-------------------")
    print("1. Add Student")
    print("2. Display Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")

    choice = int(input("Enter the choice:"))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    else:
        print("Invaild option")






