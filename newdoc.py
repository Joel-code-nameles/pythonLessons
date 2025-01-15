import customtkinter
import time
import threading

class app:
    def __init__(self,win):
        self.win = win
        self.win.geometry("1000x600")
        self.win.title("Customtkinter Complex Example")
        self.win.configure(fg_color = "#1a1717")
        customtkinter.set_appearance_mode("Light")
        customtkinter.set_default_color_theme("blue")
        self.current_mode = "Light"
        self.frames()
        

#logic
    def loadproccess(self):
        for i in range(101):
            self.pb.set(i)
            time.sleep(5)

    def thredingprossces(self):
        threading.Thread(target=self.loadproccess,daemon= True).start()

    def switchtheme(self):
        if self.current_mode == "Light":
            customtkinter.set_appearance_mode("Dark")
            customtkinter.set_default_color_theme("blue")
            self.current_mode = "dark"
            
        
        

#cases
    def frames(self):
        self.firstframe = customtkinter.CTkFrame(self.win,width = 200,height= 600,fg_color= "#262525")
        self.firstframe.place(rely = 0,relx = 0)

        self.firstlbl = customtkinter.CTkLabel(self.firstframe,text="CustomTkinter",font=("Comic Sans MS",20),text_color="white")
        self.firstlbl.place(rely = 0,relx = 0.1)

        self.firstbutt = customtkinter.CTkButton(self.firstframe,height= 30,text="CTkButton1",font=("Comic Sans MS",16,"bold"),fg_color="#858181")
        self.firstbutt.place(rely = 0.2,relx = 0.2)

        self.secondbutt = customtkinter.CTkButton(self.firstframe,height= 30,text="CTkButton2",font=("Comic Sans MS",16,"bold"),fg_color="#858181")
        self.secondbutt.place(rely = 0.3,relx = 0.2)

        self.thirdbutt = customtkinter.CTkButton(self.firstframe,height= 30,text="CTkButton3",font=("Comic Sans MS",16,"bold"),fg_color="#858181")
        self.thirdbutt.place(rely = 0.4,relx = 0.2)

        self.firstsw = customtkinter.CTkSwitch(self.firstframe,text="CTkSwitch",text_color="white")
        self.firstsw.place(rely = .8,relx = 0.2)

        self.secondsw = customtkinter.CTkSwitch(self.firstframe,text="Dark Mode",text_color="white",command=self.switchtheme())
        self.secondsw.place(rely = .9,relx = 0.2)

        self.secondframe = customtkinter.CTkFrame(self.win,width = 750,height= 550,fg_color= "#262525")
        self.secondframe.place(rely = .05,relx = .21)

        self.thirdframe = customtkinter.CTkFrame(self.secondframe,width= 450,height = 270,fg_color="black")
        self.thirdframe.place(rely = 0.05,relx = 0.1)

        self.text = customtkinter.CTkTextbox(self.thirdframe,width=380,height = 200,fg_color= "#b3b3b3",text_color="white")
        self.text.place(rely = 0.05,relx = 0.08)
       
        self.firstslider = customtkinter.CTkSlider(self.secondframe,width=450)
        self.firstslider.place(rely = 0.7,relx = 0.09)

        self.secondslider = customtkinter.CTkSlider(self.secondframe,width=450)
        self.secondslider.place(rely = 0.6,relx = 0.09)

        self.firstcbox = customtkinter.CTkCheckBox(self.secondframe,text="ChechBox disabled",text_color="gray")
        self.firstcbox.place(rely = 0.8,relx = 0.08)

        self.secondcbox = customtkinter.CTkCheckBox(self.secondframe,text="CTkChechBox",text_color="white")
        self.secondcbox.place(rely = 0.8,relx = 0.5)

        self.entry = customtkinter.CTkEntry(self.secondframe,placeholder_text="CTkEntry",text_color="gray",width= 450,fg_color="#262525")
        self.entry.place(rely = 0.9,relx = 0.07)

        self.secondlbl = customtkinter.CTkLabel(self.secondframe,text="CTkRadioButton Group",font=("Comic Sans MS",20,"bold"),text_color="white")
        self.secondlbl.place(rely = 0,relx = 0.7)

        self.thirdcbox= customtkinter.CTkCheckBox(self.secondframe,text = "CTkRadioButton",corner_radius=30,text_color="white")
        self.thirdcbox.place(rely = 0.1,relx = 0.75)

        self.fourthcbox= customtkinter.CTkCheckBox(self.secondframe,text = "CTkRadioButton",corner_radius=30,text_color="white")
        self.fourthcbox.place(rely = 0.2,relx = 0.75)

        self.fifthcbox= customtkinter.CTkCheckBox(self.secondframe,text = "CTkRadioButton",corner_radius=30,text_color="gray")
        self.fifthcbox.place(rely = 0.3,relx = 0.75)

        self.firstbutt = customtkinter.CTkButton(self.secondframe,height= 30,text="CTkButton",font=("Comic Sans MS",16,"bold"))
        self.firstbutt.place(rely = 0.9,relx = 0.75)

        self.secondbutt = customtkinter.CTkButton(self.secondframe,height= 30,text="CTkButton",font=("Comic Sans MS",16,"bold"),fg_color="gray",border_color="white")
        self.secondbutt.place(rely = 0.7,relx = 0.75)

        self.thirdbutt = customtkinter.CTkButton(self.secondframe,height= 30,text="CTkButton",font=("Comic Sans MS",16,"bold"))
        self.thirdbutt.place(rely = 0.6,relx = 0.75)

        self.fourthbutt = customtkinter.CTkButton(self.secondframe,height= 30,text="Disable Button",font=("Comic Sans MS",16,"bold"),text_color="gray")
        self.fourthbutt.place(rely = 0.5,relx = 0.75)

        self.pb = customtkinter.CTkProgressBar(self.thirdframe,width= 430,)
        self.pb.place(rely = .9,relx = 0.03)
        self.pb.set(0)

        self.tbutton = customtkinter.CTkButton(self.thirdframe,width= 2,command=self.thredingprossces)
        self.tbutton.place(rely = .3,relx = 0.9)
        self.thredingprossces()





win_app = customtkinter.CTk()
object_instance = app(win_app)
win_app.mainloop()