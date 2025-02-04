from PIL import Image
import customtkinter

window = customtkinter.CTk()
window.geometry("800x600")
window.title("Images")

imageLabel1 = customtkinter.CTkLabel(window,text="")
imageLabel1.pack()

img_url1 = r"img\tech.jpg"
image_copy1 = Image.open(img_url1)
fix_image1 = customtkinter.CTkImage(image_copy1, size=(1000,800))
imageLabel1.configure(image = fix_image1)


window.mainloop()