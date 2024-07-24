from customtkinter import *

app = CTk()
app.geometry("500x400")


slider = CTkSlider(master=app)

slider.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()