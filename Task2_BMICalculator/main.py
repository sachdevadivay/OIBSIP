import tkinter as tk
from tkinter import messagebox
from datetime import datetime


# Store BMI history
bmi_history = []


# -------------------------------
# Calculate BMI
# -------------------------------
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height_cm = float(height_entry.get())

        # Validate input
        if weight <= 0 or height_cm <= 0:
            raise ValueError

        # Convert height from cm to metres
        height_m = height_cm / 100

        # BMI formula
        bmi = weight / (height_m ** 2)

        # Determine BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal Weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        # Display result
        bmi_value.config(text=f"{bmi:.2f}")
        category_value.config(text=category)

        # Save BMI history
        date = datetime.now().strftime("%d-%m-%Y %H:%M")
        bmi_history.append((date, bmi))

        # Show result
        messagebox.showinfo(
            "BMI Result",
            f"Your BMI is {bmi:.2f}\nCategory: {category}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid positive numbers for weight and height."
        )


# -------------------------------
# Show BMI History
# -------------------------------
def show_history():
    if not bmi_history:
        messagebox.showinfo(
            "BMI History",
            "No BMI records available."
        )
        return

    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("450x350")
    history_window.resizable(False, False)

    title = tk.Label(
        history_window,
        text="BMI History",
        font=("Arial", 18, "bold")
    )
    title.pack(pady=15)

    for number, (date, bmi) in enumerate(bmi_history, 1):
        record = tk.Label(
            history_window,
            text=f"Record {number}:  {date}  →  BMI: {bmi:.2f}",
            font=("Arial", 11)
        )
        record.pack(anchor="w", padx=20, pady=5)


# -------------------------------
# Show BMI Trend
# -------------------------------
def show_trend():
    if not bmi_history:
        messagebox.showinfo(
            "BMI Trend",
            "No BMI records available."
        )
        return

    trend_text = "BMI Trend\n\n"

    for number, (date, bmi) in enumerate(bmi_history, 1):
        trend_text += (
            f"Record {number}: "
            f"{date}  →  BMI: {bmi:.2f}\n"
        )

    messagebox.showinfo(
        "BMI Trend",
        trend_text
    )


# -------------------------------
# Clear Input Fields
# -------------------------------
def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    bmi_value.config(text="--")
    category_value.config(text="--")


# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()

root.title("BMI Calculator")
root.geometry("500x550")
root.resizable(False, False)


# -------------------------------
# Heading
# -------------------------------
title_label = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold")
)
title_label.pack(pady=25)


# -------------------------------
# Input Frame
# -------------------------------
input_frame = tk.Frame(root)
input_frame.pack(pady=10)


# Weight
weight_label = tk.Label(
    input_frame,
    text="Weight (kg):",
    font=("Arial", 12)
)
weight_label.grid(
    row=0,
    column=0,
    padx=10,
    pady=10
)

weight_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)
weight_entry.grid(
    row=0,
    column=1,
    padx=10,
    pady=10
)


# Height
height_label = tk.Label(
    input_frame,
    text="Height (cm):",
    font=("Arial", 12)
)
height_label.grid(
    row=1,
    column=0,
    padx=10,
    pady=10
)

height_entry = tk.Entry(
    input_frame,
    width=20,
    font=("Arial", 12)
)
height_entry.grid(
    row=1,
    column=1,
    padx=10,
    pady=10
)


# -------------------------------
# Calculate Button
# -------------------------------
calculate_button = tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    width=20,
    font=("Arial", 11, "bold")
)
calculate_button.pack(pady=20)


# -------------------------------
# Result Frame
# -------------------------------
result_frame = tk.Frame(root)
result_frame.pack(pady=10)


# BMI
bmi_label = tk.Label(
    result_frame,
    text="BMI:",
    font=("Arial", 14, "bold")
)
bmi_label.grid(
    row=0,
    column=0,
    padx=25,
    pady=10
)

bmi_value = tk.Label(
    result_frame,
    text="--",
    font=("Arial", 14)
)
bmi_value.grid(
    row=0,
    column=1,
    padx=25,
    pady=10
)


# Category
category_label = tk.Label(
    result_frame,
    text="Category:",
    font=("Arial", 14, "bold")
)
category_label.grid(
    row=1,
    column=0,
    padx=25,
    pady=10
)

category_value = tk.Label(
    result_frame,
    text="--",
    font=("Arial", 14)
)
category_value.grid(
    row=1,
    column=1,
    padx=25,
    pady=10
)


# -------------------------------
# Buttons
# -------------------------------
button_frame = tk.Frame(root)
button_frame.pack(pady=25)


# History Button
history_button = tk.Button(
    button_frame,
    text="History",
    command=show_history,
    width=15
)
history_button.grid(
    row=0,
    column=0,
    padx=5,
    pady=5
)


# Trend Button
trend_button = tk.Button(
    button_frame,
    text="BMI Trend",
    command=show_trend,
    width=15
)
trend_button.grid(
    row=1,
    column=0,
    padx=5,
    pady=5
)


# Clear Button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    width=15
)
clear_button.grid(
    row=1,
    column=1,
    padx=5,
    pady=5
)


# -------------------------------
# Footer
# -------------------------------
footer_label = tk.Label(
    root,
    text="BMI = Weight (kg) / Height² (m²)",
    font=("Arial", 10)
)
footer_label.pack(
    side=tk.BOTTOM,
    pady=15
)


# -------------------------------
# Start Application
# -------------------------------
root.mainloop()
