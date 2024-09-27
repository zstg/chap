import sys
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageDraw
import pystray
from pystray import MenuItem, Icon

# Function to create an icon for the system tray
def create_image(width, height):
    image = Image.new('RGB', (width, height), (255, 255, 255))
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 4, height // 4, width * 3 // 4, height * 3 // 4),
        fill=(0, 128, 255))
    return image

# Function to handle the input prompt and calculation
def calculate():
    ROOT = tk.Tk()
    ROOT.withdraw()  # Hide the main window

    # Show input dialog
    user_input = simpledialog.askstring("Input", "Enter calculation (e.g., 2 + 2):")

    if user_input:
        try:
            # Evaluate the expression safely
            result = eval(user_input, {"__builtins__": None}, {})
            messagebox.showinfo("Result", f"The result is: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

# Create a system tray icon
def on_quit(icon, item):
    icon.stop()

icon = Icon("calculator")
icon.icon = create_image(64, 64)
icon.title = "Simple Calculator"
icon.menu = pystray.Menu(MenuItem('Calculate', calculate), MenuItem('Quit', on_quit))

# Run the icon
icon.run()
