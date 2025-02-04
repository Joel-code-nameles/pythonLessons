import customtkinter
import tkinter

class notepad:
    def __init__(self,notepad_application):
        self.notepad_application = notepad_application
        self.notepad_application.geometry("700x700+300+300")
        self.notepad_application.title("Notepad Clone")
        self.notepad_application.configure(fg_color = "white")
        self.NotepadContent()
        self.menu()


    def NotepadContent(self):
        self.menubar = customtkinter.CTkFrame(self.notepad_application,width = 700,height = 40,corner_radius=5,fg_color="#f4f7f0",border_width=1)
        self.menubar.pack()

        self.textArea = customtkinter.CTkTextbox(self.notepad_application,width=700,height=630,fg_color="white",border_width=0.5,font=("American Typewriter",14))
        self.textArea.place(relx = 0,rely = .057)

        self.footer = customtkinter.CTkFrame(self.notepad_application,width = 700,height = 40,corner_radius=5,fg_color="#f4f7f0",border_width=1)
        self.footer.place(relx=0,rely = 0.957)
        
    def menu(self):
        self.fileMenu = customtkinter.CTkButton(self.menubar,text="File",fg_color="transparent",text_color="black",hover=None,width=5)
        self.fileMenu.place(relx= 0.01,rely = 0.2)

        self.editmenu = customtkinter.CTkButton(self.menubar,text="Edit",fg_color="transparent",text_color="black",hover=None,width=5)
        self.editmenu.place(relx = 0.06,rely = 0.2)
    
        self.viewmenu = customtkinter.CTkButton(self.menubar,text="View",fg_color="transparent",text_color="black",hover=None,width=5)
        self.viewmenu.place(relx = 0.11,rely = 0.2)

notepad_application_window = customtkinter.CTk()
object_instance = notepad(notepad_application_window)
notepad_application_window.mainloop()        