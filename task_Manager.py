import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_description, start_date, end_date):
        task = {
            'description': task_description,
            'start_date': start_date,
            'end_date': end_date,
            'completed': False
        }
        self.tasks.append(task)
        print(f"Task '{task_description}' added.")

    def delete_task(self, task_index):
        try:
            removed_task = self.tasks.pop(task_index)
            print(f"Task '{removed_task['description']}' deleted.")
        except IndexError:
            print("Invalid task number!")

    def display_tasks(self):
        return self.tasks

    def mark_task_completed(self, task_index):
        try:
            self.tasks[task_index]['completed'] = True
            print(f"Task '{self.tasks[task_index]['description']}' marked as completed.")
        except IndexError:
            print("Invalid task number!")

class TaskManagerGUI:
    def __init__(self, root):
        self.task_manager = TaskManager()
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("600x500")  # Increase window size
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Task Manager", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
        self.label.pack(pady=10)

        self.task_description_label = tk.Label(self.frame, text="Task Description:", font=("Helvetica", 12), bg="#f0f0f0")
        self.task_description_label.pack(anchor="w")
        self.task_description_entry = tk.Entry(self.frame, width=50)
        self.task_description_entry.pack(pady=5)

        self.start_date_label = tk.Label(self.frame, text="Start Date (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f0f0f0")
        self.start_date_label.pack(anchor="w")
        self.start_date_entry = tk.Entry(self.frame, width=50)
        self.start_date_entry.pack(pady=5)

        self.end_date_label = tk.Label(self.frame, text="End Date (YYYY-MM-DD):", font=("Helvetica", 12), bg="#f0f0f0")
        self.end_date_label.pack(anchor="w")
        self.end_date_entry = tk.Entry(self.frame, width=50)
        self.end_date_entry.pack(pady=5)

        self.add_task_btn = tk.Button(self.frame, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        self.add_task_btn.pack(pady=10)

        self.tasks_listbox = tk.Listbox(self.frame, width=50, height=10, font=("Helvetica", 12))
        self.tasks_listbox.pack(pady=10)

        self.delete_task_btn = tk.Button(self.frame, text="Delete Task", command=self.delete_task, bg="#f44336", fg="white", font=("Helvetica", 12, "bold"))
        self.delete_task_btn.pack(side="left", padx=10)

        self.mark_completed_btn = tk.Button(self.frame, text="Mark as Completed", command=self.mark_task_completed, bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"))
        self.mark_completed_btn.pack(side="right", padx=10)

        self.display_tasks_btn = tk.Button(self.frame, text="Display All Tasks", command=self.display_all_tasks, bg="#FFC107", fg="black", font=("Helvetica", 12, "bold"))
        self.display_tasks_btn.pack(pady=10)

        self.update_task_listbox()

    def add_task(self):
        task_description = self.task_description_entry.get()
        start_date = self.start_date_entry.get()
        end_date = self.end_date_entry.get()
        self.task_manager.add_task(task_description, start_date, end_date)
        self.update_task_listbox()
        self.clear_entries()

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.task_manager.delete_task(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def mark_task_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.task_manager.mark_task_completed(selected_task_index[0])
            self.update_task_listbox()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")

    def display_all_tasks(self):
        all_tasks_window = tk.Toplevel(self.root)
        all_tasks_window.title("All Tasks")
        all_tasks_window.geometry("600x400")  # Set size of the new window
        all_tasks_window.configure(bg="#f0f0f0")

        task_listbox = tk.Listbox(all_tasks_window, width=80, height=15, font=("Helvetica", 12))
        task_listbox.pack(pady=20)

        tasks = self.task_manager.display_tasks()
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            task_info = f"{index}. {task['description']} [{status}]"
            task_dates = f"   Start Date: {task['start_date']}, End Date: {task['end_date']}"
            task_listbox.insert(tk.END, task_info)
            task_listbox.insert(tk.END, task_dates)

        close_button = tk.Button(all_tasks_window, text="Close", command=all_tasks_window.destroy, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        close_button.pack(pady=10)

    def update_task_listbox(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = self.task_manager.display_tasks()
        for index, task in enumerate(tasks, start=1):
            status = "Completed" if task['completed'] else "Pending"
            task_info = f"{index}. {task['description']} [{status}]"
            task_dates = f"   Start Date: {task['start_date']}, End Date: {task['end_date']}"
            self.tasks_listbox.insert(tk.END, task_info)
            self.tasks_listbox.insert(tk.END, task_dates)

    def clear_entries(self):
        self.task_description_entry.delete(0, tk.END)
        self.start_date_entry.delete(0, tk.END)
        self.end_date_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = TaskManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
