
import json
import os


class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 35:
            return "D"
        return "Fail"

    def display(self):
        print(f"Name       : {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Marks      : {self.marks}")
        print(f"Grade      : {self.calculate_grade()}")

    def to_dict(self):
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks
        }


class StudentManager:
    FILE_NAME = "students.json"

    def __init__(self):
        self.students = []
        self.load_students()

    def save_students(self):
        try:
            data = [s.to_dict() for s in self.students]
            with open(self.FILE_NAME, "w") as file:
                json.dump(data, file, indent=4)
        except OSError:
            print("Error: Could not save student records.")

    def load_students(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

            for item in data:
                self.students.append(
                    Student(
                        item["name"],
                        item["roll_no"],
                        item["marks"]
                    )
                )
        except (OSError, json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Could not load student records.")

    def add_student(self):
        name = input("Enter name: ").strip()
        roll_no = input("Enter roll number: ").strip()

        if not name or not roll_no:
            print("Name and roll number cannot be empty.")
            return

        if any(s.roll_no == roll_no for s in self.students):
            print("Roll number already exists!")
            return

        try:
            marks = float(input("Enter marks (0-100): "))
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return
        except ValueError:
            print("Enter valid numeric marks.")
            return

        student = Student(name, roll_no, marks)
        self.students.append(student)
        self.save_students()
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        for student in self.students:
            print("\n--------------------")
            student.display()

    def search_student(self):
        roll_no = input("Enter roll number: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent found:")
                student.display()
                return

        print("Student not found!")

    def update_student(self):
        roll_no = input("Enter roll number to update: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                name = input(
                    f"New name [{student.name}]: "
                ).strip()
                marks_input = input(
                    f"New marks [{student.marks}]: "
                ).strip()

                if name:
                    student.name = name

                if marks_input:
                    try:
                        marks = float(marks_input)
                        if not 0 <= marks <= 100:
                            print("Marks must be between 0 and 100.")
                            return
                        student.marks = marks
                    except ValueError:
                        print("Invalid marks.")
                        return

                self.save_students()
                print("Student updated successfully!")
                return

        print("Student not found!")

    def delete_student(self):
        roll_no = input("Enter roll number to delete: ").strip()

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                self.save_students()
                print("Student deleted successfully!")
                return

        print("Student not found!")

    def run(self):
        while True:
            print("\n===== STUDENT MANAGEMENT SYSTEM =====")
            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Exit")

            choice = input("Enter choice (1-6): ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.view_students()
            elif choice == "3":
                self.search_student()
            elif choice == "4":
                self.update_student()
            elif choice == "5":
                self.delete_student()
            elif choice == "6":
                print("Thank you!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    manager = StudentManager()
    manager.run()
