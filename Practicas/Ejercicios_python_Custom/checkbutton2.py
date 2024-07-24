import tkinter as tk

eSTE POR AHORA NO FUNCIONO
def mostrar():
    if(x.get() == 1):
        print("Estas de acuerdo")
    else:
        print("No estas de acuedo")

app = tk.Tk()
app.geometry("300x100")
x = IntVar()

check_button = tk.Checkbutton(app,
                            text="Acepto",
                            Variable=x,
                            onvalue= 1,
                            ofvalue = 0,
                           command=mostrar,)

check_button.pack()


app.mainloop()