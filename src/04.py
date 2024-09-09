from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def messages(button_id):
    try:
        messagebox.showinfo("Información", f"Botón {button_id} presionado")
    except ValueError:
        pass

root = Tk()
root.title("3x3 Button")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

for i in range(3):
    for j in range(3):
        button_id = i * 3 + j + 1
        ttk.Button(mainframe, text=f"Button {button_id}", command=lambda b=button_id: messages(b)).grid(column=j, row=i+1, sticky=(W, E), padx=5, pady=5)

root.bind("<Return>", lambda event: messages("Return"))
root.mainloop()
