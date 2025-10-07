import tkinter as tk

def load_template(parent):
    frame = tk.Frame(parent, bg="lightblue", padx=10, pady=10)
    label = tk.Label(frame, text="Loaded Template", bg="lightblue")
    label.pack()
    return frame