import time
import pyautogui
import tkinter as tk
from tkinter import messagebox

def take_screenshot():
    delay = delay_var.get()
    filename = filename_var.get()

    if not filename:
        messagebox.showwarning("Missing filename", "Please enter a file name.")
        return

    try:
        delay = int(delay)
    except ValueError:
        messagebox.showerror("Invalid delay", "Delay must be an integer.")
        return

    status_var.set(f"Waiting {delay} seconds...")
    root.update()
    time.sleep(delay)

    full_path = f"C:/Users/Mi/Desktop/{filename}.png"
    img = pyautogui.screenshot(full_path)
    img.show()
    status_var.set(f"Screenshot saved: {filename}.png")

# GUI Setup
root = tk.Tk()
root.title("Interactive Screenshot Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

# Filename input
tk.Label(frame, text="Filename:").grid(row=0, column=0, sticky="e")
filename_var = tk.StringVar()
tk.Entry(frame, textvariable=filename_var, width=30).grid(row=0, column=1, padx=5)

# Delay input
tk.Label(frame, text="Delay (sec):").grid(row=1, column=0, sticky="e")
delay_var = tk.StringVar(value="5")
tk.Entry(frame, textvariable=delay_var, width=5).grid(row=1, column=1, sticky="w", padx=5)

# Buttons
tk.Button(frame, text="Take Screenshot", command=take_screenshot).grid(row=2, column=0, pady=10)
tk.Button(frame, text="Quit", command=root.destroy).grid(row=2, column=1, pady=10, sticky="e")

# Status label
status_var = tk.StringVar()
tk.Label(root, textvariable=status_var, fg="blue").pack(pady=5)

root.mainloop()
