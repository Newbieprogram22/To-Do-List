import customtkinter as ct
import tkinter as tk

# database
import mysql.connector

# defining the database connections parameters
username = "root"
password = "Fuck_of@05"
host = "127.0.0.1"
database = "todo_list"
task_table_name = "tasks"
user_table_name = "user_table"

# Creating a connection object
conn = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object
cursor = conn.cursor()

class TaskManager(ct.CTkFrame):
    # Getting user id
    user = ""
    def get_user_id(self, user_id):
        query = f"SELECT user_email FROM {user_table_name} WHERE user_email = '{user_id}'"
        cursor.execute(query)
        TaskManager.user = cursor.fetchone()[0]
        # print(result)

    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)

        # Button Functions

        # Function to add task to database
        def add_task():
            # getting task from entry
            task_name = entry_task_name.get()
            # getting task description from entry
            task_description = entry_description.get("1.0", "end")

            if task_name.strip() == "":
                tk.messagebox.showerror("Error", "Task name cannot be empty!")
                return
            
            # adding task to database
            cursor.execute(f"INSERT INTO {task_table_name} (task_name, task_description, created_by) VALUES ('{task_name}', '{task_description}', '{TaskManager.user}' )")
            conn.commit()
            tk.messagebox.showinfo("Success", "Task added successfully!")
            # clearing the entry
            entry_task_name.delete(0, "end")
            entry_description.delete("1.0", "end")

        # Function to view all tasks from the database
        def view_tasks():
            cursor.execute(f"SELECT * FROM {task_table_name} WHERE created_by = '{TaskManager.user}'")
            tasks = cursor.fetchall()
            list_tasks.delete(0, "end")
            for task in tasks:
                completed_status = "Yes" if task[3] else "No"
                list_tasks.insert("end", f"Task ID: {task[0]}, Task Name: {task[1]}, Description: {task[2]}, Completed: {completed_status}")

        # Function to view all tasks from database
        def mark_completed():
            try:
                task_id = int(entry_task_id.get())
                cursor.execute(f"UPDATE {task_table_name} SET task_status = 1 WHERE task_id = {task_id} ")
                conn.commit()
                tk.messagebox.showinfo("Success", "Task marked as completed!")
                entry_task_id.delete(0, "end")
            except ValueError:
                tk.messagebox.showerror("Error", "Task ID should be a valid integer!")


        # Function to update task details in the database
        def update_task():
            try:
                task_id = int(entry_task_id.get())
                task_name = entry_task_name.get()
                description = entry_description.get("1.0", "end")
                
                if task_name.strip() == "":
                    tk.messagebox.showerror("Error", "Task name cannot be empty!")
                    return
                
                cursor.execute(f"UPDATE {task_table_name} SET task_name = '{task_name}', task_description = '{description}' WHERE task_id = '{task_id}'")
                conn.commit()
                tk.messagebox.showinfo("Success", "Task details updated successfully!")
                entry_task_id.delete(0, "end")
                entry_task_name.delete(0, "end")
                entry_description.delete("1.0", "end")
            except ValueError:
                tk.messagebox.showerror("Error", "Task ID should be a valid integer!")

        # Function to delete a task from the database
        def delete_task():
            try:
                task_id = int(entry_task_id.get())
                cursor.execute(f"DELETE FROM {task_table_name} WHERE task_id = '{task_id}'")
                conn.commit()
                tk.messagebox.showinfo("Success", "Task deleted successfully!")
                entry_task_id.delete(0, "end")
            except ValueError:
                tk.messagebox.showerror("Error", "Task ID should be a valid integer!")


        # Widgets

        # Frame of Labels and Entry for adding task
        add_frame = ct.CTkFrame(self, width=0)
        add_frame.grid_columnconfigure(1, weight=1)
        add_frame.pack(fill="x", expand=True, side="top")

        ct.CTkLabel(add_frame, text="Task Name:", font=("Century Gothic", 15)).grid(row=0, column=0, padx=(5,20), pady=5)
        entry_task_name = ct.CTkEntry(add_frame, width=400)
        entry_task_name.grid(row=0, column=1, padx=5, pady=5)

        ct.CTkLabel(add_frame, text="Description:", font=("Century Gothic", 15)).grid(row=1, column=0, padx=(5,20), pady=5)
        entry_description = ct.CTkTextbox(add_frame, width=400, height=40)
        entry_description.grid(row=1, column=1, padx=5, pady=5)

        add_button = ct.CTkButton(add_frame, text="Add Task", command=add_task)
        add_button.grid(row=2, column=1, padx=5, pady=5)

        # Frame to display task
        display_frame = ct.CTkFrame(self, width=0)
        display_frame.pack(fill="x", expand=True, side="top")

        # list_tasks = tk.Listbox(display_frame, width=80, height=10)
        list_tasks = tk.Listbox(display_frame, height=10, fg="white", bg="#0F0F0F")
        # list_tasks.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
        list_tasks.pack(fill="x", expand=True, side="top")

        view_button = ct.CTkButton(display_frame, text="View Tasks", command=view_tasks)
        # view_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2)
        view_button.pack(side="top")

        # Frame of task operations
        # Frame and widgets for marking as completed, updating, and deleting tasks
        operation_frame = ct.CTkFrame(self)
        # operation_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
        operation_frame.pack(fill="x", expand=True, side="top")

        ct.CTkLabel(operation_frame, text="Task ID:").grid(row=0, column=0, padx=5, pady=5)
        entry_task_id = ct.CTkEntry(operation_frame, width=50)
        entry_task_id.grid(row=0, column=1, padx=5, pady=5)

        mark_button = ct.CTkButton(operation_frame, text="Mark Completed", command=mark_completed)
        mark_button.grid(row=0, column=2, padx=5, pady=5)

        update_button = ct.CTkButton(operation_frame, text="Update Task", command=update_task)
        update_button.grid(row=0, column=3, padx=5, pady=5)

        delete_button = ct.CTkButton(operation_frame, text="Delete Task", command=delete_task)
        delete_button.grid(row=0, column=4, padx=5, pady=5)

        # Exit button
        exit_button = ct.CTkButton(self, text="Exit", command=self.quit)
        # exit_button.grid(row=2, column=2, padx=5, pady=20)
        exit_button.pack(fill="x", expand=True, side="bottom")
