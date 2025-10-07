import tkinter as tk
import requests
import json
from z_template.sidebar import create_sidebar
from z_template.body import create_body


def layout():
    """
    Creates a Tkinter window and sets its minimum size.
    """
    root = tk.Tk()
    root.title("HTX API Python312 by Airis")
    root.minsize(1000, 600)
    
    session = requests.Session()
    session.headers.update({"User-Agent": "MyApp/1.0"})

    label = tk.Label(root, text="Loading", font=("Arial", 16))
    label.pack(pady=50)

    # Use the session for all requests
    response = session.get("https://httpbin.org/get")
    print(response.json())
    
    # hide label
    label.pack_forget()

    

    sidebar = create_sidebar(root)
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    body = create_body(root)
    body.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    root.mainloop()