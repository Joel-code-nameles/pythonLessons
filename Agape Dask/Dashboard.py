import customtkinter

window = customtkinter.CTk()
window.geometry("1300x760")
window.title("Agape Desk")

border1 = customtkinter.CTkFrame(window,width= 1300,height=49,fg_color= "#A20025",corner_radius= 0)
border1.place(relx = 0,rely = 0)

border2 = customtkinter.CTkFrame(window,width= 1300,height=52,fg_color= "#A20025",corner_radius= 0)
border2.place(relx = 0,rely = 0.925)

frame = customtkinter.CTkFrame(window,width= 300,height= 597,fg_color="#0E715B",corner_radius= 0,border_color="black",border_width= 1)
frame.place(relx = 0,rely  = 0.0717)

label = customtkinter.CTkLabel(border1,text_color="white",text ="AGAPE DESK")
label.place(relx = 0.04,rely = 0.19)

date = customtkinter.CTkLabel(border1,text_color="white",text ="December 25, 2025")
date.place(relx = 0.4,rely = 0.19)

dashboard = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "DashBoard")
dashboard.place(relx = 0.05,rely = 0.1)

reg = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "Registration")
reg.place(relx = 0.05,rely = 0.2)

data_house = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "Data House")
data_house.place(relx = 0.05,rely = 0.3)

academics = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "Academics")
academics.place(relx = 0.05,rely = 0.4)

properties = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "Properties")
properties.place(relx = 0.05,rely = 0.5)

settings = customtkinter.CTkButton(frame,width= 260,fg_color="white",border_color="black",border_width= 1,hover_color="white",text_color="Black",text= "Settings")
settings.place(relx = 0.05,rely = 0.6)

f_students = customtkinter.CTkFrame(window,width=270,height=160,fg_color="#0F8A7B",border_color="#0B44A8",border_width=2)
f_students.place(relx = 0.28,rely = 0.1)

m_students = customtkinter.CTkFrame(window,width=270,height=160,fg_color="#647687",border_color="#825F3F",border_width=2)
m_students.place(relx = 0.53,rely = 0.1)

t_students = customtkinter.CTkFrame(window,width=270,height=160,fg_color="#A20025",border_color="#8C0519",border_width=2)
t_students.place(relx = 0.78,rely = 0.1)

graph = customtkinter.CTkFrame(window,width=610,height=190,fg_color="white",border_color="black",border_width=2)
graph.place(relx = 0.28,rely = 0.38)

bar = customtkinter.CTkFrame(window,width=610,height=150,fg_color="white",border_color="black",border_width=2)
bar.place(relx = 0.28,rely = 0.68)

box1 = customtkinter.CTkFrame(window,width=170,height=190,fg_color="white",border_color="black",border_width=2)
box1.place(relx = 0.78,rely = 0.38)

box2 = customtkinter.CTkFrame(window,width=170,height=150,fg_color="white",border_color="black",border_width=2)
box2.place(relx = 0.78,rely = 0.68)

profile = customtkinter.CTkFrame(border1,width=30,height=30,fg_color="white",border_color="black",border_width=2,corner_radius=360)
profile.place(relx = 0.925,rely = 0.29)

window.mainloop()