from tkinter import *
from tkinter import ttk

def messages(*args):
    try:
        message.set("Hola tontos menos el doc y yo")
    except ValueError:
        pass

root = Tk()
root.geometry("300x100")
root.title("Message with button")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), )
root.columnconfigure(0, weight=2)
root.rowconfigure(0, weight=2)

message = StringVar()
ttk.Label(mainframe, textvariable=message).grid(column=2, row=1, sticky=(W, E), padx=5, pady=5)
ttk.Button(mainframe, text="Message", command=messages).grid(column=1, row=1, sticky=(W, E))

root.bind("<Return>", messages)
root.mainloop()