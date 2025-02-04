import customtkinter

class Registration:
    def __init__(self,window):
        self.window = window
        self.window.geometry("600x600")
        self.window.title("registration")
        self.window.configure(fg_color = "blue")

        self.reg_form()

    def reg_form(self):
        self.navigation = customtkinter.CTkFrame(self.window,height=60,width=700,fg_color="black")
        self.navigation.place(relx=0,rely=0)



win = customtkinter.CTk()
obj = Registration(win)
win.mainloop()
