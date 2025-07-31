import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"Your BMI is: {bmi}\nCategory: {category}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for weight and height.")

# Create window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x250")
window.resizable(False, False)

# Weight input
tk.Label(window, text="Enter your weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack(pady=5)

# Height input
tk.Label(window, text="Enter your height (m):").pack(pady=5)
height_entry = tk.Entry(window)
height_entry.pack(pady=5)

# Calculate Button
tk.Button(window, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 10))
result_label.pack(pady=10)

# Run the application
window.mainloop()
