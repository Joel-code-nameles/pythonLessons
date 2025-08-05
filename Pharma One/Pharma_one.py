import customtkinter

win = customtkinter.CTk()
win.geometry("1300x760")
win.title("Pharma One")

#navigation
nav = customtkinter.CTkFrame(win,width= 300,height= 730,fg_color="#283342",corner_radius= 0)
nav.place(relx = 0,rely  = 0.0889)

frame1 = customtkinter.CTkFrame(win,width= 1000,height= 65,fg_color="#F7FAFD",corner_radius= 0)
frame1.place(relx = 0.23,rely  = 0)

frame2 = customtkinter.CTkFrame(win,width= 300,height= 65,fg_color="#1D242E",corner_radius= 0)
frame2.place(relx = 0,rely  = 0)

dashboard = customtkinter.CTkLabel(nav,text_color= "white",text= "DashBoard",font=("MS UI Gothic",20))
dashboard.place(relx = 0.01,rely = 0.09)

inventory = customtkinter.CTkLabel(nav,text_color= "white",text= "Inventory",font=("MS UI Gothic",20))
inventory.place(relx = 0.01,rely = 0.14)

reports = customtkinter.CTkLabel(nav,text_color= "white",text= "Reports",font=("MS UI Gothic",20))
reports.place(relx = 0.01,rely = 0.19)

configure = customtkinter.CTkLabel(nav,text_color= "white",text= "Configure",font=("MS UI Gothic",20))
configure.place(relx = 0.01,rely = 0.24)

c_management = customtkinter.CTkLabel(nav,text_color= "white",text= "Contact Management",font=("MS UI Gothic",20))
c_management.place(relx = 0.01,rely = 0.31)

notification = customtkinter.CTkLabel(nav,text_color= "white",text= "Notification",font=("MS UI Gothic",20))
notification.place(relx = 0.01,rely = 0.36)

icon = customtkinter.CTkFrame(nav,width= 9,height= 9,fg_color="#F0483E",corner_radius= 360)
icon.place(relx = 0.56,rely = 0.37)

c_w_v = customtkinter.CTkLabel(nav,text_color= "white",text= "Chat With Visitor",font=("MS UI Gothic",20))
c_w_v.place(relx = 0.01,rely = 0.41)

app_settings = customtkinter.CTkLabel(nav,text_color= "white",text= "Application Settings",font=("MS UI Gothic",20))
app_settings.place(relx = 0.01,rely = 0.49)

C_19 = customtkinter.CTkLabel(nav,text_color= "white",text= "Covid - 19",font=("MS UI Gothic",20))
C_19.place(relx = 0.01,rely = 0.54)

g_t_h = customtkinter.CTkLabel(nav,text_color= "white",text= "Get Technical Help",font=("MS UI Gothic",20))
g_t_h.place(relx = 0.01,rely = 0.59)

frame3 = customtkinter.CTkFrame(nav,width= 40,height= 40,fg_color="white",corner_radius= 2)
frame3.place(relx = 0.02,rely = 0.02)

g_dot = customtkinter.CTkFrame(nav,width= 9,height= 9,fg_color="#2ED47A",corner_radius= 360)
g_dot.place(relx = 0.136,rely = 0.0437)

#content

i_status = customtkinter.CTkFrame(win,width=240,height=150,fg_color="white",border_color="#3CB98B",border_width=2)
i_status.place(relx = 0.24,rely = 0.17)

i_status_details = customtkinter.CTkFrame(win,width=240,height=40,fg_color="#A6CBCB",border_color="#3CB98B",border_width=2)
i_status_details.place(relx = 0.24,rely = 0.35)

i_status2 = customtkinter.CTkFrame(win,width=240,height=150,fg_color="white",border_color="#FEE040",border_width=2)
i_status2.place(relx = 0.43,rely = 0.17)

i_status_details2 = customtkinter.CTkFrame(win,width=240,height=40,fg_color="#F2E9AC",border_color="#FEE040",border_width=2)
i_status_details2.place(relx = 0.43,rely = 0.35)

i_status3 = customtkinter.CTkFrame(win,width=240,height=150,fg_color="white",border_color="#55C3F5",border_width=2)
i_status3.place(relx = 0.62,rely = 0.17)

i_status_details3 = customtkinter.CTkFrame(win,width=240,height=40,fg_color="#A7DCF5",border_color="#55C3F5",border_width=2)
i_status_details3.place(relx = 0.62,rely = 0.35)

i_status4 = customtkinter.CTkFrame(win,width=240,height=150,fg_color="white",border_color="#F0483E",border_width=2)
i_status4.place(relx = 0.812,rely = 0.17)

i_status_details4 = customtkinter.CTkFrame(win,width=240,height=40,fg_color="#EEBFBF",border_color="#F0483E",border_width=2)
i_status_details4.place(relx = 0.812,rely = 0.35)

box = customtkinter.CTkFrame(win,width=470,height=190,fg_color="white",border_color="black",border_width=2)
box.place(relx = 0.24,rely = 0.43)

box1 = customtkinter.CTkFrame(win,width=470,height=190,fg_color="white",border_color="black",border_width=2)
box1.place(relx = 0.62,rely = 0.43)

box2 = customtkinter.CTkFrame(win,width=470,height=185,fg_color="white",border_color="black",border_width=2)
box2.place(relx = 0.24,rely = 0.73)

box3 = customtkinter.CTkFrame(win,width=470,height=185,fg_color="white",border_color="black",border_width=2)
box3.place(relx = 0.62,rely = 0.73)

searchbar = customtkinter.CTkEntry(frame1,width=400,height=40,placeholder_text="Search anything?")
searchbar.place(relx = 0.01,rely = 0.2)

circle = customtkinter.CTkFrame(frame1,width= 20,height= 20 ,fg_color= "orange",corner_radius=360)
circle.place(relx = 0.8,rely = 0.004)

lale = customtkinter.CTkLabel(frame1,text_color="black",text=" Good Morning\n14 January 2022 22:45:04")
lale.place(relx = 0.83,rely = 0.004)


win.mainloop()