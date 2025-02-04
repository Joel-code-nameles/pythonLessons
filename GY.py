import tkinter
import customtkinter

window = customtkinter.CTk()
window.title("Z-Tech")
window.geometry("300x520")

# Navigation
navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="red")
navigation_frame.place(relx = 0,rely = 0)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="orange")
navigation_frame.place(relx = 0,rely = 0.15)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="yellow")
navigation_frame.place(relx = 0,rely = 0.30)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="green")
navigation_frame.place(relx = 0,rely = 0.45)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="blue")
navigation_frame.place(relx = 0,rely = 0.60)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="purple")
navigation_frame.place(relx = 0,rely = 0.75)

navigation_frame = customtkinter.CTkFrame(window,width=300,height=60,fg_color="pink")
navigation_frame.place(relx = 0,rely = 0.90)



window.mainloop()