import random
import json
import tkinter
from PIL import Image, ImageTk

selected_list = "undefined"
aura_level = 0
aura_point = 0

current_aura_image = None


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

    with open("oopwork.json", "r", encoding="utf8") as file:
        auras = json.load(file)

    filtered_auras = [
        aura for aura in auras
        if aura["list"] == selected_list
    ]

    weights = [aura["chance"] for aura in filtered_auras]

    rolled_aura = random.choices(filtered_auras, weights=weights, k=1)[0]

    print("You rolled:", rolled_aura["name"])

    aura_point += rolled_aura["aura_quantity"]
    print("Aura Points:", aura_point)

    return rolled_aura


root = tkinter.Tk()
root.geometry("500x500")

try:
    open_image = Image.open("Screenshot 2026-05-28 095222.jpg")
    open_image = open_image.resize((400, 300))
    current_aura_image = ImageTk.PhotoImage(open_image)

    image_label = tkinter.Label(root, image=current_aura_image)
    image_label.pack(side="top", fill="both", expand=True, pady=20)

except FileNotFoundError:
    image_label = tkinter.Label(
        root,
        text="[ JPEG Image Area ]\n(Ensure file is in the script's folder)",
        font=("Arial", 14)
    )
    image_label.pack(side="top", fill="both", expand=True)


result_label = tkinter.Label(root, text="Roll an aura!", font=("Arial", 16))
result_label.pack()

points_label = tkinter.Label(
    root,
    text="Aura Points: " + str(aura_point),
    font=("Arial", 14)
)
points_label.pack()


roll_frame = tkinter.Frame(root, bg="red")
roll_button = tkinter.Button(
    roll_frame,
    text="Roll for Auras",
    font="Player2P",
    bg="cyan",
    activebackground="red",
    bd=0
)

roll_frame.pack(side="bottom", fill="x")
roll_button.pack(side="bottom", ipady=20, fill="x", padx=5, pady=5)


def colorpress(event):
    roll_button.config(bg="red")
    roll_frame.config(bg="cyan")


def colorrelease(event):
    global current_aura_image

    roll_button.config(bg="cyan")
    roll_frame.config(bg="red")

    rolled_aura = Titles()

    result_label.config(text="You rolled: " + rolled_aura["name"])
    points_label.config(text="Aura Points: " + str(aura_point))

    try:
        open_image = Image.open(rolled_aura["image"])
        open_image = open_image.resize((400, 300))
        current_aura_image = ImageTk.PhotoImage(open_image)

        image_label.config(image=current_aura_image, text="")
        image_label.image = current_aura_image

    except FileNotFoundError:
        image_label.config(
            image="",
            text="Image not found:\n" + rolled_aura["image"]
        )


roll_button.bind("<Button-1>", colorpress)
roll_button.bind("<ButtonRelease-1>", colorrelease)

root.mainloop()