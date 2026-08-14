import tkinter as tk
from tkinter import messagebox
import random
import string

# Generate Password
def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        characters = ""

        if var_upper.get():
            characters += string.ascii_uppercase
        if var_lower.get():
            characters += string.ascii_lowercase
        if var_digits.get():
            characters += string.digits
        if var_symbols.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number.")

# Copy Password
def copy_password():
    password = password_entry.get()

    if password == "":
        messagebox.showwarning("Warning", "Generate a password first.")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()

    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Clear
def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    var_upper.set(True)
    var_lower.set(True)
    var_digits.set(True)
    var_symbols.set(False)

# GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x450")
root.resizable(False, False)

title = tk.Label(
    root,
    text="Password Generator",
    font=("Arial", 22, "bold")
)
title.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

tk.Label(
    frame,
    text="Password Length:",
    font=("Arial", 12)
).grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(frame, width=10, font=("Arial", 12))
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=False)

options = tk.LabelFrame(root, text="Include Characters", padx=15, pady=10)
options.pack(pady=15)

tk.Checkbutton(options, text="Uppercase (A-Z)", variable=var_upper).pack(anchor="w")
tk.Checkbutton(options, text="Lowercase (a-z)", variable=var_lower).pack(anchor="w")
tk.Checkbutton(options, text="Numbers (0-9)", variable=var_digits).pack(anchor="w")
tk.Checkbutton(options, text="Symbols (!@#$)", variable=var_symbols).pack(anchor="w")

tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    width=22,
    font=("Arial", 11, "bold")
).pack(pady=15)

password_entry = tk.Entry(
    root,
    width=35,
    font=("Arial", 14),
    justify="center"
)
password_entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="Copy",
    command=copy_password,
    width=12
).grid(row=0, column=0, padx=8)

tk.Button(
    btn_frame,
    text="Clear",
    command=clear_fields,
    width=12
).grid(row=0, column=1, padx=8)

footer = tk.Label(
    root,
    text="Generate secure random passwords using Python",
    font=("Arial", 9)
)
footer.pack(side=tk.BOTTOM, pady=10)

root.mainloop()
