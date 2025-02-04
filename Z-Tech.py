import tkinter
import customtkinter
from tkinter.messagebox import showwarning


def login():
    showwarning("Invalid", "Incorrect Username and Password",parent =main_window)

main_window = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
main_window.geometry("330x600+0+0")
main_window.title("Z-tech")


navigation = customtkinter.CTkFrame(main_window,height = 60,width = 330,fg_color="#21acde")
navigation.place(relx = 0,rely =0)

brandname = customtkinter.CTkLabel(navigation,text="Z-TECH", font=("times new roman",20,"bold"),text_color="black")
brandname.place(relx = 0.05,rely =0.2)

username = customtkinter.CTkEntry(main_window,placeholder_text="Username", font=("times new roman",16), width= 250,corner_radius=30)
username.place(relx = 0.1,rely = 0.2)

password = customtkinter.CTkEntry(main_window,placeholder_text="Password", font=("times new roman",16), width= 250,corner_radius=30,show = "*")
password.place(relx = 0.1,rely = 0.3)


button = customtkinter.CTkButton(main_window, width = 250, text= "Login",fg_color="#21acde",font=("times new roman",16),command=login)
button.place(relx = 0.1,rely = 0.4)









main_window.mainloop()
