from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("ElektronikKu")

window.state("zoomed")  
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
bg_img = Image.open("background.jpg")
bg_img = bg_img.resize((width, height))         
bg_photo = ImageTk.PhotoImage(bg_img)

canvas = Canvas(window, width=width, height=height)
canvas.pack(fill="both", expand=True)

canvas.create_image(0,0, image=bg_photo, anchor="nw")

canvas.create_text(width//2, 100, anchor="center", text="Elektronikku", fill="#D7C097", font=("Roboto", 64))

button = Button(window, 
                text="Click Me", 
                font=("Arial", 20, "bold"),
                bg="#4B7BE5",     
                fg="white",
                activebackground="#3A67C8",
                activeforeground="white",
                relief="flat",
                padx=20,
                pady=10)
button_window = canvas.create_window(width//3, 300, anchor="center", window=button)

window.mainloop()