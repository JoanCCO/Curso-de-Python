from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")

btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="#2E8B57",
                hover_color="#FF4500", border_color="#FFCC70",
                border_width=2,)
                
        

btn.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()