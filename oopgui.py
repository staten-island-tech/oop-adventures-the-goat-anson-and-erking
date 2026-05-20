import tkinter
root = tkinter.Tk()

root.geometry("500x500")
roll_frame = tkinter.Frame(root, bg="red")
roll_button = tkinter.Button(roll_frame, text = "Roll for Auras", font="Player2P", bg="cyan", activebackground="red", bd=0)
roll_frame.pack(side="bottom", fill="x")
roll_button.pack(side = "bottom", ipady=20, fill="x", padx=5, pady=5)

def colorpress(event):
    roll_button.config(bg="red")
    roll_frame.config(bg="cyan")
    
def colorrelease(event):
    roll_button.config(bg="cyan")
    roll_frame.config(bg="red")
    
roll_button.bind("<Button-1>", colorpress)
roll_button.bind("<ButtonRelease-1>", colorrelease)

root.mainloop()