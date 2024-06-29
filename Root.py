# importing important modules
import tkinter
import customtkinter as ct
from PIL import ImageTk, Image

# importing files
import Login, Register, Task

# appearance of the window
ct.set_appearance_mode("system")
ct.set_default_color_theme("blue")


class Main(ct.CTk):
    def __init__(self):
        super().__init__()
        self.frames = {}  # initializing an empty array to store frames
        self.geometry("600x500")
        self.title("ToDo List")
        self.bg_img = ImageTk.PhotoImage(Image.open("pattern.png"))
        self.img_label = ct.CTkLabel(self, image=self.bg_img, text="")
        self.img_label.pack()
        self.store_frames(Login.LoginManager, Register.RegisterManager, Task.TaskManager)
        self.show_frame(Login.LoginManager)
        self.mainloop()

    def store_frames(self,*args):
        for F in (args):
            # frame = F(app, img_label, corner_radius=15)
            # frames[F] = frame
            self.frames[F] = F(self, master=self.img_label, corner_radius=15)

    def show_frame(self, current_frame):
        frame = self.frames[current_frame]
        if (current_frame == Task.TaskManager):
            frame.grid(row=0, column=0, sticky="nsew")
            # frame.pack()
        else:
            frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        frame.tkraise()



app = Main()