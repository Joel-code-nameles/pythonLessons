import customtkinter
import main
from tkinter import messagebox

class Idk:
    def __init__(self,win):
        self.win = win
        self.win.geometry("700x500")
        self.win.resizable(0,0)
        self.win.title("Mini Project")
        customtkinter.set_appearance_mode("dark")
        self.register()

    def register(self):
        self.username = customtkinter.CTkEntry(self.win,width = 300,placeholder_text="Username",font=("MS UI Gothic",12.525))
        self.username.place(relx = 0.3,rely = 0.3)

        self.phone_num = customtkinter.CTkEntry(self.win,width = 300,placeholder_text="Phone Number (+233)",font=("MS UI Gothic",12.525))
        self.phone_num.place(relx = 0.3,rely = 0.4)

        self.btn = customtkinter.CTkButton(self.win,width = 50,text= "ADD",corner_radius= 20,fg_color= "Green",command= self.insert_data)
        self.btn.place(relx = 0.47,rely = 0.5)


    def insert_data(self):
        if(self.username.get() and self.phone_num.get()):
            main.insert_data(self.username.get(), self.phone_num.get())
            messagebox.showinfo("User Added", f"{self.username.get()} Contact Added successfully")


root = customtkinter.CTk()
obj = Idk(root)
root.mainloop()