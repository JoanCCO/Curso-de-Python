from customtkinter import *

app = CTk()
app.geometry("500x400")

combobox = CTkComboBox(master=app, values=["Seleccione Opcion","Carro", "Moto", "Bicicleta"],fg_color="#0093E9",
                border_color="#FBAB7E", dropdown_fg_color="#0093E9")

combobox.place(relx=0.5, rely=0.5, anchor="center")

app.mainloop()