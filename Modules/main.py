import  customtkinter
win = customtkinter.CTk()
win.geometry("300x500")


def mainfrom():
    user = customtkinter.CTkEntry(win,placeholder_text="Username",width=250)
    user.place(relx = 0.03,rely = 0.3)

    phonenum = customtkinter.CTkEntry(win,placeholder_text="Phone Number",width=250)
    phonenum.place(relx = 0.03,rely = 0.4)

    subit = customtkinter.CTkButton(win,height=20,width=40,text= "Submit",corner_radius=30,command=contactlist)
    subit.place(relx = 0.35,rely = 0.5)

    win.mainloop()

    usern = user.get()
    phonenu = phonenum.get()

    lable = customtkinter.CTkLabel(win,text= "",)
    