import tkinter
root = tkinter.Tk()

root.geometry("500x500")
roll_button = tkinter.Button(root, text = "Roll for Auras")
roll_button.pack(side = "bottom", pady=20, padx=90)

root.mainloop()