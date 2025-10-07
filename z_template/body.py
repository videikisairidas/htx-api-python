import tkinter as tk

# def 
def create_body(parent):
    frame = tk.Frame(parent, bg="lightblue", padx=10, pady=10)
    label = tk.Label(frame, text="Start Using!", bg="lightblue", font=("Arial", 16))
    label.pack()
    return frame