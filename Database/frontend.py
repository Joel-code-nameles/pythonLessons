import  customtkinter
from PIL import Image
import databaseCode

class Reg:
    def __init__(self,mainFrame):
        self.mainFrame = mainFrame
        self.mainFrame.geometry("400x600")
        self.mainFrame.resizable(0,0)
        self.mainFrame.title("Red Panda")
        self.register()
        self.image()


    def register(self):
        self.username = customtkinter.CTkEntry(self.mainFrame,placeholder_text="Username",width=300,font=("Sniglet",12),corner_radius=30)
        self.username.place(relx = 0.16,rely = 0.3)

        self.password =  customtkinter.CTkEntry(self.mainFrame,placeholder_text="Password",width=300,font=("Sniglet",12),corner_radius=30,show = "#")
        self.password.place(relx = 0.16,rely = 0.36)

        self.button = customtkinter.CTkButton(self.mainFrame,text="Submit",font=("Sniglet",12),corner_radius=30,fg_color="#F55536",hover_color="#FF773D",command= self.insert_data)
        self.button.place(relx = 0.35,rely = 0.42)

    def insert_data(self):
      if (self.username.get() and self.password.get()):
          databaseCode.insert_data(self.username.get(), self.password.get())


    def image(self):
        self.imageLabel1 = customtkinter.CTkLabel(self.mainFrame, text="")
        self.imageLabel1.place(relx=0.43, rely=0.1)

        self.img_url1 = r"image/cute-cartoon-red-panda2.png"
        self.image_copy1 = Image.open(self.img_url1)
        self.fix_image1 = customtkinter.CTkImage(self.image_copy1, size=(70, 70))
        self.imageLabel1.configure(image=self.fix_image1)

        self.lal = customtkinter.CTkLabel(self.mainFrame, text_color= "#FF0800",text="Red Panda",font=("Sniglet",40))
        self.lal.place(relx = 0.27,rely = 0.02)


root = customtkinter.CTk()
obj = Reg(root)
root.mainloop()