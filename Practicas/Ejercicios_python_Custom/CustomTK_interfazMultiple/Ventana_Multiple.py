from customtkinter import *

app = CTk()
app.geometry("500x400")
app.title('Base de Datos')

frame = CTkScrollableFrame(master=app, fg_color="#BFBF00", border_color="#0000FF", border_width=2,
                           orientation="vertical", scrollbar_button_color="#FF4500")
frame.pack(expand=True)

label = CTkLabel(master=frame, text_color="#000000", text="Enter Name")
entry = CTkEntry(master=frame, placeholder_text="Name...")
btn = CTkButton(master=frame, text="Submit")

label.pack(anchor='s', expand=True, pady=10, padx=30)
entry.pack(anchor='s', expand=True, pady=10, padx=30)
btn.pack(anchor='n', expand=True, pady=30, padx=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True, padx=30, pady=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True, padx=30, pady=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True, padx=30, pady=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True, padx=30, pady=20)
CTkButton(master=frame, text="Another Widget").pack(expand=True, padx=30, pady=20)


app.mainloop()
