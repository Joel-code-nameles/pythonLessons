import tkinter
import customtkinter
from tkinter.messagebox import showinfo
app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app.resizable(0,0)
app.geometry("700x600+0+0")
app.title("Agape Acadamy International")

    

#navigation
navigation = customtkinter.CTkFrame(app,height=60,width=700,fg_color="black")
navigation.place(relx=0,rely=0)

lbl = customtkinter.CTkLabel(navigation,text="Agape Acadamy International School",text_color="purple",font=("new times roman",20,"bold"))
lbl.place(relx = 0.1,rely = 0.2)

#frame2
frame2 = customtkinter.CTkFrame(app,fg_color="black",height=300,width=350)
frame2.place(relx = 0.2,rely = 0.3)

lbl2 = customtkinter.CTkLabel(frame2,text="Login",text_color="white",font=("new times roman",18,"bold"))
lbl2.place(relx = 0.45,rely = 0)

username = customtkinter.CTkEntry(frame2,placeholder_text="Username",width=150,corner_radius=30)
username.place(relx=0.3,rely=0.2)

password = customtkinter.CTkEntry(frame2,placeholder_text="Password",width=150,corner_radius=30,show = ("."))
password.place(relx=0.3,rely=0.4)

loginb = customtkinter.CTkButton(frame2,text="Login",text_color="black",fg_color="purple",hover_color="magenta")
loginb.place(relx = 0.3,rely = 0.7)
app.mainloop()
