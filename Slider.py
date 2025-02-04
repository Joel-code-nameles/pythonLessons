import customtkinter

application = customtkinter.CTk()
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
application.geometry("500x50")
application.title("Speaker/HP")

def VolumeValue(value):
    print(f"Slider Volume{value}")



Volume = customtkinter.CTkSlider(master=application,from_=0,command=VolumeValue)
Volume.pack()
application.mainloop()
