# importing important modules
import tkinter
import customtkinter as ct
# importing files
import Register, Task

# database
import mysql.connector

# defining the database connections parameters
username = "root"
password = "Fuck_of@05"
host = "127.0.0.1"
database = "todo_list"
table_name = "user_table"

# Creating a connection object
conn = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object
cursor = conn.cursor()


# Login class
class LoginManager(ct.CTkFrame):

    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets ->
        
        self.login_label = ct.CTkLabel(self, text="Login to your Account", font=("Century Gothic", 20))
        self.login_label.grid(row=0, column=0, columnspan=3, padx=40, pady=20)

        self.user_entry = ct.CTkEntry(self, width=220, placeholder_text="Email ID",  corner_radius=8)
        self.user_entry.grid(row=1, column=0, columnspan=3, padx=40, pady=20)
        
        self.pwd_entry = ct.CTkEntry(self, width=220, placeholder_text="Password", corner_radius=8, show='*')
        self.pwd_entry.grid(row=2, column=0, columnspan=3, padx=40, pady=20)

        # Button functions
        def forget_pwd():
            pass

        def login_app():
            self.place_forget()
            root.show_frame(Task.TaskManager)

        def login_function():
            user_email = self.user_entry.get()
            pwd_entry = self.pwd_entry.get()
            details = (user_email != "") and (pwd_entry != "")
            if details:
                # login logic
                # select_query = f"SELECT * FROM {table_name}"
                # cursor.execute(select_query)
                # results = cursor.fetchall()
                # for row in results:
                #     print(row)

                query = "SELECT user_email, user_pwd FROM user_table WHERE user_email = %s"

                cursor.execute(query, (user_email,))

                result = cursor.fetchone()

                if result:
                    user_name = result[0]
                    stored_pwd = result[1]
                    print(f"User Name: {user_name}, Password: {stored_pwd}")
                    if pwd_entry == stored_pwd:
                        Task.TaskManager.get_user_id(self, user_name)
                        login_app()
                    else:
                        tkinter.messagebox.showerror("Error", "Password does not match")
                        self.pwd_entry.delete(0, "end")
                        self.pwd_entry.focus_set()
                else:
                    tkinter.messagebox.showerror("Error", "User does not exist")
                    self.user_entry.delete(0, "end")
                    self.pwd_entry.delete(0, "end")
                    self.user_entry.focus_set()
                    print("User not found!")
            else:
                tkinter.messagebox.showerror("Error", "Please fill all the fields")

        # self.forget_pwd_btn = ct.CTkButton(self, text="Forget Password", text_color="white", fg_color="transparent", width=0)
        # self.forget_pwd_btn.grid(row=3, column=2)

        self.login_btn = ct.CTkButton(self, text="Login", corner_radius=6, width=220, command=login_function)
        self.login_btn.grid(row=4, column=0, padx=40, pady=(20, 10), columnspan=3)
        
        self.register_btn = ct.CTkButton(self, text="Register User", corner_radius=6, width=220, command=lambda: root.show_frame(Register.RegisterManager))
        self.register_btn.grid(row=5, column=0, padx=40, pady=20, columnspan=3)
