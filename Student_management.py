import tkinter as tk
from tkinter import messagebox

class Student:
    def __init__(self, name, roll_number, age, grade, address):
        self.name = name
        self.roll_number = roll_number
        self.age = age
        self.grade = grade
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_number}, Age: {self.age}, Grade: {self.grade}, Address: {self.address}"

class StudentManagementSystem:
    def __init__(self, root):
        self.students = []
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("500x600")
        
        self.frame = tk.Frame(root)
        self.frame.pack(pady=20)

        # Title Label
        self.label = tk.Label(self.frame, text="Student Management System", font=("Arial", 16))
        self.label.pack(pady=10)

        # Buttons
        self.add_student_btn = tk.Button(self.frame, text="Add Student", font=("Arial", 12), width=30, command=self.add_student)
        self.add_student_btn.pack(pady=5)

        self.view_students_btn = tk.Button(self.frame, text="View Students", font=("Arial", 12), width=30, command=self.view_students)
        self.view_students_btn.pack(pady=5)

        self.update_student_btn = tk.Button(self.frame, text="Update Student", font=("Arial", 12), width=30, command=self.update_student)
        self.update_student_btn.pack(pady=5)

        self.delete_student_btn = tk.Button(self.frame, text="Delete Student", font=("Arial", 12), width=30, command=self.delete_student)
        self.delete_student_btn.pack(pady=5)

        self.exit_btn = tk.Button(self.frame, text="Exit", font=("Arial", 12), width=30, command=root.quit, bg="red", fg="white")
        self.exit_btn.pack(pady=10)

    def add_student(self):
        def submit_student():
            name = name_entry.get()
            roll_number = roll_number_entry.get()
            age = age_entry.get()
            grade = grade_entry.get()
            address = address_entry.get()

            if name and roll_number and age and grade and address:
                student = Student(name, roll_number, age, grade, address)
                self.students.append(student)
                messagebox.showinfo("Success", "Student added successfully!")
                add_student_window.destroy()
            else:
                messagebox.showerror("Error", "All fields are required!")

        add_student_window = tk.Toplevel(self.root)
        add_student_window.title("Add Student")
        add_student_window.geometry("400x400")

        tk.Label(add_student_window, text="Name:", font=("Arial", 12)).pack(pady=5)
        name_entry = tk.Entry(add_student_window, font=("Arial", 12))
        name_entry.pack(pady=5)

        tk.Label(add_student_window, text="Roll Number:", font=("Arial", 12)).pack(pady=5)
        roll_number_entry = tk.Entry(add_student_window, font=("Arial", 12))
        roll_number_entry.pack(pady=5)

        tk.Label(add_student_window, text="Age:", font=("Arial", 12)).pack(pady=5)
        age_entry = tk.Entry(add_student_window, font=("Arial", 12))
        age_entry.pack(pady=5)

        tk.Label(add_student_window, text="Grade:", font=("Arial", 12)).pack(pady=5)
        grade_entry = tk.Entry(add_student_window, font=("Arial", 12))
        grade_entry.pack(pady=5)

        tk.Label(add_student_window, text="Address:", font=("Arial", 12)).pack(pady=5)
        address_entry = tk.Entry(add_student_window, font=("Arial", 12))
        address_entry.pack(pady=5)

        tk.Button(add_student_window, text="Submit", font=("Arial", 12), command=submit_student).pack(pady=10)

    def view_students(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("View Students")
        view_window.geometry("500x400")

        if not self.students:
            tk.Label(view_window, text="No students to display", font=("Arial", 12)).pack(pady=20)
        else:
            for student in self.students:
                tk.Label(view_window, text=str(student), font=("Arial", 10)).pack(pady=5)

    def update_student(self):
        def submit_update():
            roll_number = roll_number_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            grade = grade_entry.get()
            address = address_entry.get()

            student_found = False
            for student in self.students:
                if student.roll_number == roll_number:
                    student.name = name
                    student.age = age
                    student.grade = grade
                    student.address = address
                    student_found = True
                    break

            if student_found:
                messagebox.showinfo("Success", "Student details updated successfully!")
                update_student_window.destroy()
            else:
                messagebox.showerror("Error", "Student with given roll number not found!")

        update_student_window = tk.Toplevel(self.root)
        update_student_window.title("Update Student")
        update_student_window.geometry("400x400")

        tk.Label(update_student_window, text="Roll Number:", font=("Arial", 12)).pack(pady=5)
        roll_number_entry = tk.Entry(update_student_window, font=("Arial", 12))
        roll_number_entry.pack(pady=5)

        tk.Label(update_student_window, text="Name:", font=("Arial", 12)).pack(pady=5)
        name_entry = tk.Entry(update_student_window, font=("Arial", 12))
        name_entry.pack(pady=5)

        tk.Label(update_student_window, text="Age:", font=("Arial", 12)).pack(pady=5)
        age_entry = tk.Entry(update_student_window, font=("Arial", 12))
        age_entry.pack(pady=5)

        tk.Label(update_student_window, text="Grade:", font=("Arial", 12)).pack(pady=5)
        grade_entry = tk.Entry(update_student_window, font=("Arial", 12))
        grade_entry.pack(pady=5)

        tk.Label(update_student_window, text="Address:", font=("Arial", 12)).pack(pady=5)
        address_entry = tk.Entry(update_student_window, font=("Arial", 12))
        address_entry.pack(pady=5)

        tk.Button(update_student_window, text="Submit", font=("Arial", 12), command=submit_update).pack(pady=10)

    def delete_student(self):
        def submit_delete():
            roll_number = roll_number_entry.get()

            student_found = False
            for student in self.students:
                if student.roll_number == roll_number:
                    self.students.remove(student)
                    student_found = True
                    break

            if student_found:
                messagebox.showinfo("Success", "Student deleted successfully!")
                delete_student_window.destroy()
            else:
                messagebox.showerror("Error", "Student with given roll number not found!")

        delete_student_window = tk.Toplevel(self.root)
        delete_student_window.title("Delete Student")
        delete_student_window.geometry("400x300")

        tk.Label(delete_student_window, text="Roll Number:", font=("Arial", 12)).pack(pady=5)
        roll_number_entry = tk.Entry(delete_student_window, font=("Arial", 12))
        roll_number_entry.pack(pady=5)

        tk.Button(delete_student_window, text="Submit", font=("Arial", 12), command=submit_delete).pack(pady=10)

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    student_management_system = StudentManagementSystem(root)
    root.mainloop()
