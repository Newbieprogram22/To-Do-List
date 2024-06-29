# importing important modules
import tkinter
import customtkinter as ct
# importing files
import Login

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

# # Create a cursor object
cursor = conn.cursor()


# Registration class
class RegisterManager(ct.CTkFrame):
    def __init__(self, root, master, **kwargs):
        super().__init__(master, **kwargs)

        # Widgets ->

        self.register_label = ct.CTkLabel(self, text="Create New Account", font=("Century Gothic", 20))
        self.register_label.grid(row=0, column=0, columnspan=3, padx=40, pady=20)

        self.firstname_entry = ct.CTkEntry(self, placeholder_text="First Name")
        self.firstname_entry.grid(row=1, column=0, padx=40, pady=10)

        self.lastname_entry = ct.CTkEntry(self, placeholder_text="Last Name")
        self.lastname_entry.grid(row=1, column=1, padx=40, pady=10)

        self.email_entry = ct.CTkEntry(self, placeholder_text="Email", width=360)
        self.email_entry.grid(row=2, column=0, columnspan=3, padx=40, pady=10)
        
        self.contact_entry = ct.CTkEntry(self, placeholder_text="Contact", width=360)
        self.contact_entry.grid(row=3, column=0, columnspan=3, padx=40, pady=10)

        self.secQues_entry = ct.CTkEntry(self, placeholder_text="Security Question", width=360)
        self.secQues_entry.grid(row=4, column=0, columnspan=3, padx=40, pady=10)

        self.secAns_entry = ct.CTkEntry(self, placeholder_text="Answer", width=360)
        self.secAns_entry.grid(row=5, column=0, columnspan=3, padx=40, pady=10)

        self.pwd_entry = ct.CTkEntry(self, placeholder_text="Password", show='*')
        self.pwd_entry.grid(row=6, column=0, padx=40, pady=10)

        self.confirm_pwd_entry = ct.CTkEntry(self, placeholder_text="Confirm Password", show='*')
        self.confirm_pwd_entry.grid(row=6, column=1, padx=40, pady=10)

        # Button functions

        def cancel():  # cancel the registration
            self.place_forget()
            root.show_frame(Login.LoginManager)

        def register_user():  # register the user
            # Register user logic
            password = self.pwd_entry.get()
            confirm_password = self.confirm_pwd_entry.get()
            if password == confirm_password:

                # storing values in the database
                register_query = f"INSERT INTO {table_name} (user_name, user_email, user_contact, sec_ques, sec_ans, user_pwd, user_conf_pwd) VALUES {(self.firstname_entry.get() + " " + self.lastname_entry.get()), self.email_entry.get(), self.contact_entry.get(), self.secQues_entry.get(), self.secAns_entry.get(), self.pwd_entry.get(), self.confirm_pwd_entry.get()}"
                # select_query = f"SELECT * FROM {table_name} WHERE user_name = '{username}'"
                cursor.execute(register_query)
                conn.commit()
                cursor.close()
                conn.close()

                # message box
                tkinter.messagebox.showinfo("Register User", "Registration Successful")

                # going back to login window
                self.place_forget()
                root.show_frame(Login.LoginManager)
            else:
                tkinter.messagebox.showerror("Error", "Password does not match")

        def register_func():  # register verify
            mand_detail = (self.firstname_entry.get() != "") and (self.email_entry.get() != "") and (self.contact_entry.get() != "")
            mand_security = (self.secQues_entry.get() != "") and (self.secAns_entry.get() != "")
            mand_pwd = (self.pwd_entry.get() != "") and (self.confirm_pwd_entry.get() != "")
            result = mand_detail and mand_security and mand_pwd
            if (result):
                register_user()
            else:
                tkinter.messagebox.showerror("Error", "Please fill all the fields")

        self.register_btn = ct.CTkButton(self, text="Register", command=register_func)
        self.register_btn.grid(row=7, column=0, padx=40, pady=20)

        self.cancel_btn = ct.CTkButton(self, text="Cancel", command=cancel)
        self.cancel_btn.grid(row=7, column=1, padx=40, pady=20)
