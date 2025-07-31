import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    if length <= 0:
        messagebox.showwarning("Warning", "Please enter a valid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Create window
root = tk.Tk()
root.title("Simple Password Generator")
root.geometry("400x200")
root.config(padx=20, pady=20)

# Length label and entry
tk.Label(root, text="Enter Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Result entry
tk.Label(root, text="Generated Password:").pack()
result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

# Run the app
root.mainloop()
