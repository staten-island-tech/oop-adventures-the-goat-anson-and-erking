#IDEA : WHALEN RNG
import random
current_luck = 0
aura_point = 10000000
def Titles():
    if aura_point >= 1000000000000000000:
        print("WHALEN AURA POINTS")
    elif aura_point >= 100000000000:
        print("Mogger Sub 5 Whalen Aura Points")
    elif aura_point >= 1000000000:
        print("Extrodinary Aura Points")      
    elif aura_point >= 100000000:''
        print("Very High Aura Points")  
    elif aura_point >= 10000000:
        print("High Aura Points")
    elif aura_point >= 10000:
        print("Medium Aura Points")
    elif aura_point >= 1000:
        print("Low Aura Points")

Titles()
import tkinter as tk
from tkinter import ttk
def main():
   root = tk.Tk()
   frm = ttk.Frame(root, padding=10)
   frm.grid()
   ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
   ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
   root.mainloop()
if __name__ == "__main__":
   main()


