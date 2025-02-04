import customtkinter
from PIL import Image

window = customtkinter.CTk()
window.geometry("1000x600")
window.title("")

navigation = customtkinter.CTkFrame(window,height=600,width=225,fg_color="#00b2cb")
navigation.place(rely = 0,relx = 0)

lbl1 = customtkinter.CTkLabel(navigation,text="Lab Boad",text_color="white",font=("times new romans",20,"bold"))
lbl1.place(rely = 0.01,relx = 0.3)

imageLabel1 = customtkinter.CTkLabel(navigation,text="")
imageLabel1.place(rely = 0.2,relx = 0.03)

img_url1 = r"img\png.png"
image_copy1 = Image.open(img_url1)
fix_image1 = customtkinter.CTkImage(image_copy1, size=(30,25))
imageLabel1.configure(image = fix_image1)

imageLabel2 = customtkinter.CTkLabel(navigation,text="",)
imageLabel2.place(rely = 0.3,relx = 0.03)

img_url2 = r"img\mail.png"
image_copy2 = Image.open(img_url2)
fix_image2 = customtkinter.CTkImage(image_copy2, size=(30,25))
imageLabel2.configure(image = fix_image2)

imageLabel3 = customtkinter.CTkLabel(navigation,text="")
imageLabel3.place(rely = 0.4,relx = 0.03)

img_url3 = r"img\upload.png"
image_copy3 = Image.open(img_url3)
fix_image3 = customtkinter.CTkImage(image_copy3, size=(30,25))
imageLabel3.configure(image = fix_image3)

imageLabel4 = customtkinter.CTkLabel(navigation,text="")
imageLabel4.place(rely = 0.5,relx = 0.03)

img_url4 = r"img\sey.png"
image_copy4 = Image.open(img_url4)
fix_image4 = customtkinter.CTkImage(image_copy4, size=(30,25))
imageLabel4.configure(image = fix_image4)

imageLabel5 = customtkinter.CTkLabel(navigation,text="")
imageLabel5.place(rely = 0.6,relx = 0.03)

img_url5 = r"img\calander.png"
image_copy5 = Image.open(img_url5)
fix_image5 = customtkinter.CTkImage(image_copy5, size=(30,25))
imageLabel5.configure(image = fix_image5)

imageLabel6 = customtkinter.CTkLabel(navigation,text="")
imageLabel6.place(rely = 0.7,relx = 0.03)

img_url6 = r"img\person.png"
image_copy6 = Image.open(img_url6)
fix_image6 = customtkinter.CTkImage(image_copy6, size=(30,25))
imageLabel6.configure(image = fix_image6)

imageLabel7 = customtkinter.CTkLabel(navigation,text="")
imageLabel7.place(rely = 0.8,relx = 0.03)

img_url7 = r"img\wiglet.png"
image_copy7 = Image.open(img_url7)
fix_image7 = customtkinter.CTkImage(image_copy7, size=(30,25))
imageLabel7.configure(image = fix_image7)

lbldashboard = customtkinter.CTkButton(navigation,text="DASHBOARD",text_color="white",font=("",16),fg_color="transparent")
lbldashboard.place(rely = 0.2,relx = 0.3)

lblmail = customtkinter.CTkButton(navigation,text="MESSAGE",text_color="white",font=("",16),fg_color="transparent")
lblmail.place(rely = 0.3,relx = 0.3)

lblleads = customtkinter.CTkButton(navigation,text="LEADS",text_color="white",font=("",16),fg_color="transparent")
lblleads.place(rely = 0.4,relx = 0.3)

lbltask = customtkinter.CTkButton(navigation,text="TASK",text_color="white",font=("",16),fg_color="transparent")
lbltask.place(rely = 0.5,relx = 0.3)

lblclander = customtkinter.CTkButton(navigation,text="CALENDER",text_color="white",font=("",16),fg_color="transparent")
lblclander.place(rely = 0.6,relx = 0.3)

lblcontact = customtkinter.CTkButton(navigation,text="CONTACT",text_color="white",font=("",16),fg_color="transparent")
lblcontact.place(rely = 0.7,relx = 0.3)

lblgrid = customtkinter.CTkButton(navigation,text="GRID",text_color="white",font=("",16),fg_color="transparent")
lblgrid.place(rely = 0.8,relx = 0.3)

frame = customtkinter.CTkFrame(window,width=400,height=150)
frame.place(relx = 0.25,rely = 0.03)

bimageLabel = customtkinter.CTkLabel(frame,text="")
bimageLabel.place(rely = 0,relx = 0)

bimg_url = r"img\bargraph.webp"
bimage_copy = Image.open(bimg_url)
bfix_image = customtkinter.CTkImage(bimage_copy, size=(400,150))
bimageLabel.configure(image = bfix_image)

frame2 = customtkinter.CTkFrame(window,width=150,height=150)
frame2.place(rely = 0.02,relx = 0.7)

frame3 = customtkinter.CTkFrame(window,width=400,height=150)
frame3.place(relx = 0.25,rely = 0.45)

frame4 = customtkinter.CTkFrame(window,width=150,height=150)
frame4.place(rely = 0.45,relx = 0.7)





window.mainloop()