import customtkinter

class CurrencyCalc:
    def __init__(self,master):
        self.master = master
        self.master.title("Currency Converter")
        self.master.geometry("400x600")
        self.login()


    def login(self):
        self.contianer = customtkinter.CTkFrame(self.master,height=600,width=400,fg_color="#1E1F22",corner_radius=0)
        self.contianer.place(relx = 0,rely = 0)

        self.username = customtkinter.CTkEntry(self.contianer,placeholder_text="Username",width=300,font=("Bahnschrift",12),corner_radius=30,fg_color="#1E1F22")
        self.username.place(relx = 0.1,rely = 0.3)

        self.password = customtkinter.CTkEntry(self.contianer,placeholder_text="Password",width=300,font=("Bahnschrift",12),corner_radius=30,fg_color="#1E1F22")
        self.password.place(relx = 0.1,rely = 0.35)

        self.loginlal = customtkinter.CTkLabel(self.contianer,text_color="#FFA050",text="</>\nLogin",font=("Bahnschrift",30,"bold"))
        self.loginlal.place(relx = 0.34,rely = 0.15)

        self.next = customtkinter.CTkButton(self.contianer,width=40,fg_color="#FFA050",text="Next",command=self.calculator)
        self.next.place(relx = 0.4,rely = 0.45)

    def calculator(self):
        self.contianer1 = customtkinter.CTkFrame(self.master,height=600,width=400,fg_color="#1E1F22",corner_radius=0)
        self.contianer1.place(relx = 0,rely = 0)

        self.nav = customtkinter.CTkFrame(self.contianer1,width=400,height=40,fg_color="#FFA050")
        self.nav.place(relx = 0,rely = 0)

        self.lal = customtkinter.CTkLabel(self.nav,text_color="black",text="</> CodeCale",font=("Bahnschrift",20,"bold"))
        self.lal.place(relx = 0.15,rely = 0.01)

        self.from_option = customtkinter.CTkOptionMenu(self.contianer1,values=["GHS","USD","CAD","Euro","GBP"],dropdown_fg_color="#1E1F22",dropdown_text_color="white")
        self.from_option.place(relx = 0.1,rely = 0.3)

        self.from_lal = customtkinter.CTkLabel(self.contianer1,text_color="White",text="From",font=("Bahnschrift",20,"bold"))
        self.from_lal.place(relx = 0.1,rely = 0.25)

        self.to_option = customtkinter.CTkOptionMenu(self.contianer1,values=["USD","GHS","CAD","Euro","GBP"],fg_color="#FFA050",dropdown_fg_color="#1E1F22",dropdown_text_color="white")
        self.to_option.place(relx = 0.5,rely = 0.3)

        self.to_lal = customtkinter.CTkLabel(self.contianer1,text_color="White",text="To",font=("Bahnschrift",20,"bold"))
        self.to_lal.place(relx = 0.5,rely = 0.25)

        self.from_entry = customtkinter.CTkEntry(self.contianer1,placeholder_text="Amt",font=("Bahnschrift",20,"bold"),fg_color="#1E1F22",corner_radius=15,text_color="white")
        self.from_entry.place(relx = 0.1,rely = 0.37)

        self.to_entry = customtkinter.CTkEntry(self.contianer1,placeholder_text="Amt",font=("Bahnschrift",20,"bold"),fg_color="#1E1F22",corner_radius=15,text_color="white")
        self.to_entry.place(relx = 0.5,rely = 0.37)

        self.con = customtkinter.CTkButton(self.contianer1,width=200,text_color="white",text="Convert",font=("Bahnschrift",20,"bold"),command=self.converter)
        self.con.place(relx = 0.24,rely = 0.45)

    def converter(self):
        if self.from_option.get() == "GHS" and self.to_option.get() == "USD":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(14.00)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate / self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "USD" and self.to_option.get() == "GHS":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(14.00)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate * self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "GHS" and self.to_option.get() == "GBP":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(18.45)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate / self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "GBP" and self.to_option.get() == "GHS":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(18.45)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate * self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif  self.from_option.get() == "CAD" and self.to_option.get() == "GHS":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(10.05)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate * self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif  self.from_option.get() == "GHS" and self.to_option.get() == "CAD":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(10.05)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate / self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "Euro" and self.to_option.get() == "GHS":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(15.70)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate * self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "GHS" and self.to_option.get() == "Euro":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(15.70)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate / self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "Euro" and self.to_option.get() == "USD":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(15.70)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate * self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)

        elif self.from_option.get() == "USD" and self.to_option.get() == "Euro":
            self.from_currency = self.from_option.get()
            self.to_currency = self.to_option.get()
            self.rate = int(14.00)
            self.amount_txt = int(self.from_entry.get())
            self.result = float(self.rate / self.amount_txt)
            self.to_entry.configure(placeholder_text=self.result)







window = customtkinter.CTk()
obj = CurrencyCalc(window)
window.mainloop()