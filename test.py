import random
import json

auras = open("./oopwork.json", encoding="utf8")
data = json.load(auras)

selected_list = "undefined"
aura_level = 0
aura_point = 10


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

    # Choose which list to roll from

    # Filter only matching auras
    filtered_auras = [
        aura for aura in auras
        if aura["list"] == selected_list
    ]

    # Get names and chances
    names = [aura["name"] for aura in filtered_auras]
    weights = [aura["chance"] for aura in filtered_auras]
    
    aura_point = [aura["aura_quantity"] for aura in filtered_auras]
    # Roll aura
    result = random.choices(names, aura_point=aura_point, weights=weights, k=1)[0]
   

    print("You rolled:", result)

Titles()




import tkinter as tk

root = tk.Tk()

def button_pressed():
    Titles()

button = tk.Button(
    root,
    text="Click Me",
    command=button_pressed
)

button.pack()

root.mainloop()