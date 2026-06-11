import random
import json

auras = open("./oopwork.json", encoding="utf8")
data = json.load(auras)

selected_list = "undefined"
aura_level = 0
aura_point = 10000000000000


def Titles():

    global selected_list
    global aura_point

    # Tier selection
    if aura_point >= 10000000000000000:
        print("Mogger High Tier Whalen Aura Points")
        selected_list = "WHALEN"

    elif aura_point >= 100000000:
        print("Extraordinary Aura Points")
        selected_list = "extraordinary"

    elif aura_point >= 10000000:
        print("High Aura Points")
        selected_list = "high"

    elif aura_point >= 10000:
        print("Medium Aura Points")
        selected_list = "medium"

    else:
        print("Low Aura Points")
        selected_list = "low"

    with open("oopwork.json", "r") as file:
        auras = json.load(file)


    filtered_auras = [
        aura for aura in auras
        if aura["list"] == selected_list
    ]
    print(filtered_auras)

    names = [aura["name"] for aura in filtered_auras]
    weights = [aura["chance"] for aura in filtered_auras]
    
    
    result = random.choices(names , weights=weights, k=1)[0]
   
    print("You rolled:", result)



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
    Titles()
roll_button.bind("<Button-1>", colorpress)
roll_button.bind("<ButtonRelease-1>", colorrelease)

root.mainloop()