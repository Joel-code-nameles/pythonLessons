import tkinter
import customtkinter
from tkinter.messagebox import showwarning


def login():
    showwarning("Invalid","Incorrect Username or Password")

app = customtkinter.CTk()
customtkinter.set_appearance_mode ("dark")
customtkinter.set_default_color_theme("dark-blue")
app.geometry("300x500+0+0")
app.title("wiremee")


#NAV Bar
nav_bar = customtkinter.CTkFrame(app,height=60,width=330,fg_color="black")
nav_bar.place(relx = 0,rely = 0)

name = customtkinter.CTkLabel(nav_bar,text="wiremee", font=("times new ronam",20,"bold"),text_color="red")
name.place(relx = 0.010,rely=0.2)
username = customtkinter.CTkEntry(app,placeholder_text="Username", font=("times new roman",16), width= 250,corner_radius=30)
username.place(relx = 0.1,rely = 0.2)

password = customtkinter.CTkEntry(app,placeholder_text="Password", font=("times new roman",16), width= 250,corner_radius=30,show = "*")
password.place(relx = 0.1,rely = 0.3)


button = customtkinter.CTkButton(app, width = 250, text= "Login",text_color= ("black"),fg_color="#03fc4a",font=("times new roman",16),command=login,hover_color=("black"))
button.place(relx = 0.1,rely = 0.4)
app.mainloop()


