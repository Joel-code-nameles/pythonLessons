import customtkinter

app = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
app.resizable(0,0)
app.geometry("700x700+0+0")
app.title("Code Town")

def main():
    user = username.get()
    bir = birth.get()
    full = fullname.get()
    nationality
    print(f"Username: {user}, Birth Place : {bir}")

#navigation
navigation = customtkinter.CTkFrame(app,height=60,width=700,fg_color="black")
navigation.place(relx=0,rely=0)

Signup = customtkinter.CTkLabel(navigation,text="Sign Up", font=("times new ronam",20,"bold"),text_color="yellow")
Signup.place(relx = 0.010,rely=0.2)

fullname = customtkinter.CTkEntry(app,placeholder_text="Fullname", font=("times new roman",16), width= 250,corner_radius=30)
fullname.place(relx = 0.1,rely = 0.2)

birth = customtkinter.CTkEntry(app,placeholder_text="Date of Birth",font=("times new roman",16), width=250,corner_radius=30)
birth.place(relx= 0.1,rely = 0.3)

place = customtkinter.CTkEntry(app,placeholder_text="Place of Birth",font=("times new roman",16), width=250,corner_radius=30)
place.place(relx = 0.1,rely=0.4)

nationality = customtkinter.CTkEntry(app,placeholder_text="Nationality",font=("times new roman",16), width=250,corner_radius=30)
nationality.place(relx=0.1,rely=0.5)

username = customtkinter.CTkEntry(app,placeholder_text="Username", font=("times new roman",16), width= 250,corner_radius=30)
username.place(relx = 0.1,rely = 0.6)


interest = customtkinter.CTkEntry(app,placeholder_text="Interests", font=("Arial",16),width=250,corner_radius=30)
interest.place(relx = 0.5,rely= 0.2)

Github = customtkinter.CTkEntry(app,placeholder_text="Github Account Name", font=("Arial",16),width=250,corner_radius=30)
Github.place(relx = 0.5,rely= 0.3)

language = customtkinter.CTkEntry(app,placeholder_text="Coding Language", font=("Arial",16),width=250,corner_radius=30)
language.place(relx = 0.5,rely= 0.4)

Experience = customtkinter.CTkEntry(app,placeholder_text="Expirence[yes/no]", font=("Arial",16),width=250,corner_radius=30)
Experience.place(relx = 0.5,rely= 0.5)

location = customtkinter.CTkEntry(app,placeholder_text="Location", font=("Arial",16),width=250,corner_radius=30)
location.place(relx = 0.5,rely= 0.6)

submit = customtkinter.CTkButton(app,width=20,text= "Login",text_color= ("black"),fg_color="yellow",font=("times new roman",16),)
submit.place(relx = 0.4,rely = 0.8)

















app.mainloop()