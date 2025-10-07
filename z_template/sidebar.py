# sidebar.py
import tkinter as tk

def create_sidebar(parent_frame):
    """
    Creates and configures a sidebar Frame with a fixed pixel width.
    """
    # Set a fixed width of 350 pixels for the sidebar
    sidebar_frame = tk.Frame(parent_frame, width=200, bg="#f0f0f0", relief=tk.SUNKEN, borderwidth=2)
    
    # Pack the sidebar to the left and make it fill the vertical space
    sidebar_frame.pack(side=tk.LEFT, fill=tk.Y)
    
    # Prevent the frame from shrinking to fit its contents
    # This is crucial for maintaining the fixed width
    sidebar_frame.pack_propagate(False)

    # Add widgets to the sidebar
    sidebar_title = tk.Label(sidebar_frame, text="Sidebar", font=("Arial", 14, "bold"), bg="#f0f0f0")
    sidebar_title.pack(pady=10)
    
    button1 = tk.Button(sidebar_frame, text="Account")
    button1.pack(fill=tk.X, padx=10, pady=5)

    button2 = tk.Button(sidebar_frame, text="Spot")
    button2.pack(fill=tk.X, padx=10, pady=15)

    button3 = tk.Button(sidebar_frame, text="Margin")
    button3.pack(fill=tk.X, padx=10, pady=25)
    
    return sidebar_frame