import customtkinter

class registration:
    def __init__(self,reg):
        self.reg = reg
        self.reg.geometry("600x600")
        self.reg.title("registration")
        self.reg.configure(fg_color = "black")

#cases
    def boxes(self):
        self.firstn = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="First Name",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.firstn.place(relx = 0.2,rely = 0.06)

        self.secn = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="Last Name",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.secn.place(relx = 0.2,rely = 0.12)

        self.bob = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="Date of Birth",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.bob.place(relx = .2,rely = .18)

        self.addre = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="Address",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.addre.place(relx = .2,rely = .24)

        self.username = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="Username",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.username.place(relx = .2,rely = .30)

        self.password = customtkinter.CTkEntry(self.reg,width=400,placeholder_text="Password",text_color="white",font=("Comic Sans MS",16),border_color="white",fg_color="black")
        self.password.place(relx = .2,rely = .36)

        self.bt = customtkinter.CTkButton(self.reg,width=400,text = "Validation",font=("Comic Sans MS",16),command=self.val)
        self.bt.place(relx = .2,rely = 0.7)

    def apperance(self):
        self.apper = customtkinter.set_appearance_mode ("dark")
        self.apper = customtkinter.set_default_color_theme("dark-blue") 

    def val(self):
        self.fin = self.firstn.get()
        self.ln = self.secn.get()
        self.bo = self.bob.get()
        self.ad = self.addre.get()
        self.usern = self.username.get()
        self.passw = self.password.get()
        self.D = [f"First Name:{self.fin},Last Name:{self.ln},Date of Birth:{self.bo},Address:{self.ad},Username:{self.usern},Password:{self.passw}"]
        print(self.D)


reg_app = customtkinter.CTk()
object_instance = registration(reg_app)
reg_app.mainloop()