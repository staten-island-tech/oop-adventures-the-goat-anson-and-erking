import tkinter
root = tkinter.Tk()

root.geometry("500x500")
roll_button = tkinter.Button(root, text = "Roll for Auras")
roll_button.pack(side = "bottom", ipady=20, fill="x")

root.mainloop()