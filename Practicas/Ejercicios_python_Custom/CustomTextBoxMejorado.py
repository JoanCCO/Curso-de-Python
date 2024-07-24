from customtkinter import *

app = CTk()
app.geometry("500x400")

def click_handler():
    print(f"Entered Value: {textbox.get('0.0', 'end')}")
    
    
textbox = CTkTextbox(master=app, scrollbar_button_color="#FF0000", corner_radius=16,
                     border_color="#BFBF00", border_width=2)
btn = CTkButton(master=app, text="Send", command=click_handler)

textbox.pack(anchor="s", expand=True, pady=10)
btn.pack(anchor="n", expand=True,)
  
app.mainloop()