import customtkinter

window = customtkinter.CTk()
window.geometry("1300x760")
window.title("Agape Desk")

border1 = customtkinter.CTkFrame(window,width= 1300,height=49,fg_color= "#A20025",corner_radius= 0)
border1.place(relx = 0,rely = 0)

border2 = customtkinter.CTkFrame(window,width= 1300,height=52,fg_color= "#A20025",corner_radius= 0)
border2.place(relx = 0,rely = 0.925)

border3 = customtkinter.CTkFrame(window,width= 1000,height=52,fg_color= "#0E715B",corner_radius= 0)
border3.place(relx = 0.2346,rely = 0.071)

frame = customtkinter.CTkFrame(window,width= 300,height= 597,fg_color="#0E716B",corner_radius= 0,border_color="black",border_width= 1)
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

box1 = customtkinter.CTkFrame(window,width=100,height=100,fg_color="white",border_color="black",border_width=2)
box1.place(relx = 0.52,rely = 0.197)

Student_ID = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tStudent ID",placeholder_text_color="Black")
Student_ID.place(relx = 0.35,rely = 0.4)

F_name = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tFull Name",placeholder_text_color="Black")
F_name.place(relx = 0.35,rely = 0.47)

dob = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tDate Of Birth",placeholder_text_color="Black")
dob.place(relx = 0.35,rely = 0.54)

Grade = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tGrade",placeholder_text_color="Black")
Grade.place(relx = 0.35,rely = 0.62)

Parent = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tParent",placeholder_text_color="Black")
Parent.place(relx = 0.59,rely = 0.4)

Contact = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tContact",placeholder_text_color="Black")
Contact.place(relx = 0.59,rely = 0.47)

E_Contacts = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tEmergency Contact",placeholder_text_color="Black")
E_Contacts.place(relx = 0.59,rely = 0.54)

Allergy = customtkinter.CTkEntry(window,width=260,fg_color="white",border_color="black",border_width= 1,placeholder_text="\tAllergy",placeholder_text_color="Black")
Allergy.place(relx = 0.59,rely = 0.62)

bar = customtkinter.CTkFrame(window,width= 570,height=100,fg_color="#0E716B",corner_radius=0)
bar.place(relx = 0.35,rely = 0.7)

button1 = customtkinter.CTkButton(bar,width= 180,height=70,fg_color="#0E716B",border_color="black",border_width=2,text="Submit",text_color="white",hover_color="#0E716B")
button1.place(relx = 0.04,rely = 0.17)

button2 = customtkinter.CTkButton(bar,width= 180,height=70,fg_color="#A20025",text="Reset",text_color="white",border_color="black",border_width=2,hover_color="#A20025")
button2.place(relx = 0.365,rely = 0.17)

button3 = customtkinter.CTkButton(bar,width= 160,height=70,fg_color="#009999",border_color="black",border_width=2,text="Upload Picture",text_color="white",hover_color="#009999")
button3.place(relx = 0.69,rely = 0.17)

window.mainloop()
