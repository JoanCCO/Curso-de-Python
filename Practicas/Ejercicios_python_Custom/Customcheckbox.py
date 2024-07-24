from customtkinter import *

app = CTk()
app.geometry("500x400")


checkbox1 = CTkCheckBox(master=app, text="Hombre")

checkbox1.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()

