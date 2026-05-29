import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("500x500")

try:
    open_image = Image.open("Screenshot 2026-05-28 095222.jpg")
    open_image = open_image.resize((400, 300)) 
    aura_image = ImageTk.PhotoImage(open_image)
    
    image_label = tkinter.Label(root, image=aura_image)
    image_label.pack(side="top", fill="both", expand=True, pady=20)
    
except FileNotFoundError:
    image_label = tkinter.Label(root, text="[ JPEG Image Area ]\n(Ensure file is in the script's folder)", font=("Arial", 14))
    image_label.pack(side="top", fill="both", expand=True)

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