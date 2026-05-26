import random
import json
import tkinter

root = tkinter.Tk()

selected_list = "undefined"
aura_level = 0
aura_point = 1000


def Titles():
    global selected_list
    global aura_point

    # Determine title tier
    if aura_point >= 10000000000000000:
        print("Mogger High Tier Whalen Aura Points")
        selected_list = "WHALEN"

    elif aura_point >= 100000000000:
        print("Extraordinary Aura Points")
        selected_list = "extraordinary"

    elif aura_point >= 10000000000:
        print("High Aura Points")
        selected_list = "high"

    elif aura_point >= 10000000:
        print("Medium Aura Points")
        selected_list = "medium"

    else:
        print("Low Aura Points")
        selected_list = "low"

    # Load aura data
    with open("oopwork.json", "r") as file:
        auras = json.load(file)

    # Filter by selected rarity list
    filtered_auras = [
        aura for aura in auras
        if aura["list"] == selected_list
    ]

    # Pick random aura
    result = random.choices(
        filtered_auras,
        weights=[aura["chance"] for aura in filtered_auras],
        k=1
    )[0]

    # Add aura points
    aura_point += result["aura_quantity"]

    print("You rolled:", result["name"])
    print("Aura gained:", result["aura_quantity"])
    print("Total aura:", aura_point)


# Example rolls
for i in range(5):
    Titles()
    print("-----")