from customtkinter import *

app = CTk()
app.geometry("500x400")


textbox = CTkTextbox(master=app)

textbox.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()