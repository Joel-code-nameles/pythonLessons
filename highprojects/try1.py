from PIL import Image
import customtkinter

window = customtkinter.CTk()
window.geometry("1000x600")
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
window.title("Acerbion Tech Limited")
imageLabel = customtkinter.CTkLabel(window,text="")
imageLabel.pack()

img_url = r"img\tech.jpg"
image_copy = Image.open(img_url)
fix_image = customtkinter.CTkImage(image_copy, size=(1000,800))
imageLabel.configure(image = fix_image)

#cases
frame = customtkinter.CTkFrame(window,width= 300,height= 250,bg_color="transparent",fg_color="black")
frame.place(rely = 0.2,relx = 0.03)

frame1 = customtkinter.CTkFrame(window,width= 300,height= 250,bg_color="transparent",fg_color="black")
frame1.place(rely = 0.2,relx = 0.3)

frame2 = customtkinter.CTkFrame(window,width= 300,height= 250,bg_color="transparent",fg_color="black")
frame2.place(rely = 0.2,relx = 0.6)

imageLabel3 = customtkinter.CTkLabel(frame1,text="")
imageLabel3.pack()

img_url3 = r"img\pic4.jpg"
image_copy3 = Image.open(img_url3)
fix_image3 = customtkinter.CTkImage(image_copy3, size=(300,250))
imageLabel3.configure(image = fix_image3)


imageLabel2 = customtkinter.CTkLabel(frame2,text="",)
imageLabel2.pack()

img_url2 = r"img\pic3.jpg"
image_copy2 = Image.open(img_url2)
fix_image2 = customtkinter.CTkImage(image_copy2, size=(300,250))
imageLabel2.configure(image = fix_image2)


imageLabel1 = customtkinter.CTkLabel(frame,text="")
imageLabel1.pack()

img_url1 = r"img\pic2.jpg"
image_copy1 = Image.open(img_url1)
fix_image1 = customtkinter.CTkImage(image_copy1, size=(300,250))
imageLabel1.configure(image = fix_image1)


window.mainloop()