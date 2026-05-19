#IDEA : WHALEN RNG
import random

choices = ["win", "lose", "draw"]
weights = [0.5, 0.3, 0.2]

result = random.choices(choices, weights=weights, k=1)[0]
print(result)
aura_point = 10000000
def Titles():
    if aura_point >= 1000000000000000000:
        print("WHALEN AURA POINTS")
    elif aura_point >= 100000000000:
        print("Mogger Sub 5 Whalen Aura Points")
    elif aura_point >= 1000000000:
        print("Extrodinary Aura Points")      
    elif aura_point >= 100000000:
        print("Very High Aura Points")  
    elif aura_point >= 10000000:
        print("High Aura Points")
    elif aura_point >= 10000:
        print("Medium Aura Points")
    elif aura_point >= 1000:
        print("Low Aura Points")




choices = ["win", "lose", "draw"]
weights = [0.5, 0.3, 0.2]

result = random.choices(choices, weights=weights, k=1)[0]
print(result)