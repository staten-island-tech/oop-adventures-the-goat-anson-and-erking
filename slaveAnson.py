#IDEA : WHALEN RNG
import random
import json
auras = open("./oopwork.json", encoding="utf8")
data = json.load(auras)


selected_list = "undefined"
aura_level = 0
aura_point = 1000






def Titles():
    aura_point = 1000
    if aura_point >= 10000000000000000:
        print("Mogger High Tier Whalen Aura Points")
        selected_list = "WHALEN"
    
    elif aura_point >= 100000000:
        print("Extrodinary Aura Points") 
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
filtered_auras = [
    aura for aura in auras
    if aura["list"] == "low"
]
result = random.choices(
    filtered_auras,
    weights=[aura["chance"] for aura in filtered_auras],
    k=1
)[0]


