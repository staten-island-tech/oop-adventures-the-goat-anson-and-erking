#IDEA : WHALEN RNG
import random
import json

with open("oopwork.json", "r") as file:
    data = json.load(file)

selected_list = "undefined"
aura_level = 0
aura_point = 10000000000000000000000
def Titles():
    if aura_point >= 100000000000:
        print("Mogger High Tier Whalen Aura Points")
        selected_list = "WHALEN"
    
    elif aura_point >= 1000000000:
        print("Extrodinary Aura Points") 
        selected_list = "extraordinary"    
    
 
    
    elif aura_point >= 10000000:
        print("High Aura Points")
        selected_list = "high"
    
    elif aura_point >= 10000:
        print("Medium Aura Points")
        selected_list = "medium"
    
    
    elif aura_point >= 1000:
        print("Low Aura Points")
        selected_list = "low"


# Load JSON file

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

    # Roll aura
    result = random.choices(names, weights=weights, k=1)[0]

    print("You rolled:", result)

Titles()