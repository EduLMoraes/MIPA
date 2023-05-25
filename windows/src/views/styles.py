from tkinter import font

def styleSheet(label = None, button = None, window = None, entry = None, error = None):
    if label:
        label["font"] = font.Font(family="Times New Roman", size=14)
        label["bg"] = "#222"

    if button:
        button["bg"] = "#00f000"
    
    if window:
        window["bg"] = "blue"
    
    if entry:
        entry["width"] = 20

    if error:
        error["bg"] = "red"