import tkinter as tk

root = tk.Tk()

def button_pressed():
    print("Button was pressed!")

button = tk.Button(
    root,
    text="Click Me",
    command=button_pressed
)

button.pack()

root.mainloop()