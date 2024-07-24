import tkinter as tk

app = tk.Tk()
app.geometry("300x100")


checkbox_value = tk.IntVar()
checkbox = tk.Checkbutton(app, text="Aceptas las Condiciones",
                          font=("Arial", 18),
                          variable=checkbox_value)
checkbox.pack()

def print_state():
    print("Checkbox state:", checkbox_value.get())
button = tk.Button(app, text="Aceptar",
                   command=print_state)   
button.pack()
app.mainloop()