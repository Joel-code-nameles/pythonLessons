import customtkinter
from PIL import Image

window = customtkinter.CTk()
window.geometry("1300x760")
window.title("Agape Desk")


border1 = customtkinter.CTkFrame(window,width= 1300,height=49,fg_color= "#A20025",corner_radius= 0)
border1.place(relx = 0,rely = 0)

self.imageLabel1 = customtkinter.CTkLabel(window, text="")
self.imageLabel1.place(relx = 0,rely = 0.07)

self.img_url1 = r"Images/project.jpg"
self.image_copy1 = Image.open(img_url1)
self.fix_image1 = customtkinter.CTkImage(self.image_copy1, size=(1300, 640))
self.imageLabel1.configure(image=fix_image1)



border2 = customtkinter.CTkFrame(window,width= 1300,height=52,fg_color= "#A20025",corner_radius= 0)
border2.place(relx = 0,rely = 0.925)

frame = customtkinter.CTkFrame(imageLabel1,height= 450,width= 300,fg_color="#05615B",corner_radius=30,bg_color='transparent')
frame.place(relx = 0.7,rely = 0.06)

School_Id = customtkinter.CTkEntry(frame,height=40,width=225,placeholder_text="\t School ID",border_color="#A20025",border_width=1,corner_radius= 30)
School_Id.place(relx = 0.14,rely = 0.2)

Password = customtkinter.CTkEntry(frame,height=40,width=225,placeholder_text="\t Password",border_color="#A20025",border_width=1,corner_radius= 30)
Password.place(relx = 0.14, rely = 0.4)

login = customtkinter.CTkButton(frame,height=40,width=225,text="Login",border_color="#A20025",border_width=1,corner_radius= 30,fg_color="#A20025")
login.place(relx = 0.14, rely = 0.6)

label = customtkinter.CTkLabel(border1,text_color="white",text ="AGAPE DESK")
label.place(relx = 0.04,rely = 0.19)

date = customtkinter.CTkLabel(border1,text_color="white",text ="December 25, 2025")
date.place(relx = 0.4,rely = 0.19)

window.mainloop()