import tkinter
import customtkinter


app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark")
app.resizable(0,0)
app.geometry("500x650+0+0")
app.title("wiremee")

#navigation
navigation = customtkinter.CTkFrame(app,height=60,width=650,fg_color="black")
navigation.place(relx=0,rely=0)

name = customtkinter.CTkLabel(navigation,text="wiremee", font=("times new roman",20,"bold"),text_color="#03fc4a")
name.place(relx = 0.010,rely=0.2)

fullname = customtkinter.CTkEntry(app,placeholder_text="Fullname", font=("times new roman",16), width= 300,corner_radius=30)
fullname.place(relx = 0.1,rely = 0.2)

birth = customtkinter.CTkEntry(app,placeholder_text="Date of Birth",font=("times new roman",16), width=300,corner_radius=30)
birth.place(relx= 0.1,rely = 0.3)

place = customtkinter.CTkEntry(app,placeholder_text="Place of Birth",font=("times new roman",16), width=300,corner_radius=30)
place.place(relx = 0.1,rely=0.4)

nationality = customtkinter.CTkEntry(app,placeholder_text="Nationality",font=("times new roman",16), width=300,corner_radius=30)
nationality.place(relx=0.1,rely=0.5)

username = customtkinter.CTkEntry(app,placeholder_text="Username", font=("times new roman",16), width= 250,corner_radius=30)
username.place(relx = 0.1,rely = 0.6)

password = customtkinter.CTkEntry(app,placeholder_text="Password", font=("times new roman",16), width= 250,corner_radius=30,show=".")
password.place(relx = 0.1,rely = 0.7)

submit = customtkinter.CTkButton(app,width=20,text= "Submit",text_color= ("black"),fg_color="#03fc4a",font=("times new roman",16),hover_color=("#7AF558"))
submit.place(relx = 0.1,rely = 0.8)

cancel = customtkinter.CTkButton(app,width=20,text= "Cancel",text_color= ("black"),fg_color="#03fc4a",font=("times new roman",16),hover_color=("#7AF558"))
cancel.place(relx = 0.5,rely = 0.8)

search = customtkinter.CTkComboBox(navigation,width=32,values=("Fees","School","Taxes","Buy QR Code","Mobile Money"),text_color= ("#03fc4a"),fg_color="green",font=("times new roman",16))
search.place(relx= 0.6,rely= 0)

app.mainloop()