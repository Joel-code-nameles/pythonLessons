import customtkinter

class calculculater:
    def __init__(self,calcu):
        self.calcu = calcu
        self.calcu.geometry("700x650")
        self.calcu.title("Calculator")
        self.calcu.configure(fg_colour = "Black")
        self.numbers()
        self.button()
        self.apperance()
        

        
# cases
    def numbers(self):
        self.first_number = customtkinter.CTkEntry(self.calcu,width=400,placeholder_text="Number",text_color="white",font=("Comic Sans MS",16),border_color="black",fg_color="black")
        self.first_number.place(relx = 0.20,rely = 0.3)

        self.second_number = customtkinter.CTkEntry(self.calcu,width=400,placeholder_text="Number(2)",text_color="white",font=("Comic Sans MS",16),border_color="black",fg_color="black")
        self.second_number.place(relx = 0.20,rely = 0.4)

    def button(self):
        self.add = customtkinter.CTkButton(self.calcu,width=30,text="+",text_color="white",font=("Comic Sans MS",16),border_color="gray",fg_color="black",hover_color="gray",command= self.additon)  
        self.add.place(relx = 0.20,rely= 0.5) 

        self.sub = customtkinter.CTkButton(self.calcu,width=30,text="-",text_color="white",font=("Comic Sans MS",16),border_color="gray",fg_color="black",hover_color="gray",command= self.subtract)  
        self.sub.place(relx = 0.26,rely= 0.5)

        self.multi = customtkinter.CTkButton(self.calcu,width=30,text="*",text_color="white",font=("Comic Sans MS",16),border_color="gray",fg_color="black",hover_color="gray",command= self.multiply)  
        self.multi.place(relx = 0.31,rely= 0.5)

        self.div = customtkinter.CTkButton(self.calcu,width=30,text="/",text_color="white",font=("Comic Sans MS",16),border_color="gray",fg_color="black",hover_color="gray",command=self.division)  
        self.div.place(relx = 0.37,rely= 0.5)

        self.Frame = customtkinter.CTkFrame(self.calcu,width=350,height=164.1)
        self.Frame.pack()

        self.lbl = customtkinter.CTkLabel(self.Frame,text="",text_color="white",font=("Comic Sans MS",16),fg_color="transparent")  
        self.lbl.place(relx = 0.01,rely= 0.4)

    def apperance(self):
        self.apper = customtkinter.set_appearance_mode ("dark")
        self.apper = customtkinter.set_default_color_theme("dark-blue")
#logic
    
        

    def additon(self):
        self.fir = float(self.first_number.get())
        self.sec = float(self.second_number.get())
        result = (self.fir + self.sec)
        self.lbl.configure(text =f"Result = {result}")

    def subtract(self):
        self.fir = float(self.first_number.get())
        self.sec = float(self.second_number.get())
        result = (self.fir - self.sec)
        self.lbl.configure(text =f"Result = {result}")  

    def multiply(self):
        self.fir = float(self.first_number.get())
        self.sec = float(self.second_number.get())
        result = (self.fir * self.sec)
        self.lbl.configure(text =f"Result = {result}")  

    def division(self):
        self.fir = float(self.first_number.get())
        self.sec = float(self.second_number.get())
        result = (self.fir / self.sec)
        self.lbl.configure(text =f"Result = {result}")


calcu_app = customtkinter.CTk()
object_instance = calculculater(calcu_app)
calcu_app.mainloop()