import tkinter as tk
import tkinter.ttk as ttk 
from tkinter import *
from ttkthemes import ThemedStyle


def create_grid():
    for i in range(2):
        for j in range(4):
            canvas.create_oval(30 + j * 100, 50 + i * 100, 70 + j * 100, 90 + i * 100, outline='black')

def on_channel_button_click(channel_count):
    print(f"{channel_count}-channel button clicked.")




# ------- main app ----------------------------------------------
app = tk.Tk()
app.title("mpo lux")
app.geometry("600x400")

# Banner
banner_label = tk.Label(app, text="mpo lux", font=("Arial", 20))
banner_label.pack(anchor=tk.NW)

# Grid
canvas = tk.Canvas(app, width=400, height=200)
canvas.pack()
create_grid()

# Buttons
button_frame = tk.Frame(app)
button_frame.pack(side=tk.RIGHT, padx=20)

channels = [8, 12, 16, 24]
for channel_count in channels:
    button = tk.Button(button_frame, text=f"{channel_count}-channel", command=lambda count=channel_count: on_channel_button_click(count))
    button.pack(pady=10)

# Footer
footer_label = tk.Label(app, text="mpo_lux - v0.01 - author: Justin Knox - aGPL License V3.0")
footer_label.pack(side=tk.BOTTOM, pady=10)

app.mainloop()
