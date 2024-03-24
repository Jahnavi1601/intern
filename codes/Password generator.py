import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    global length_entry, uppercase_var, lowercase_var, digits_var, special_var

    length = int(length_entry.get())

    # Check if at least one option is selected
    if not any((uppercase_var.get(), lowercase_var.get(), digits_var.get(), special_var.get())):
        messagebox.showerror("Error", "Please select at least one option.")
        return

    # Define character sets based on user selections
    characters = ""
    if uppercase_var.get():
        characters += string.ascii_uppercase
    if lowercase_var.get():
        characters += string.ascii_lowercase
    if digits_var.get():
        characters += string.digits
    if special_var.get():
        characters += string.punctuation

    # Ensure at least one character from each selected category
    password = ''
    if uppercase_var.get():
        password += random.choice(string.ascii_uppercase)
    if lowercase_var.get():
        password += random.choice(string.ascii_lowercase)
    if digits_var.get():
        password += random.choice(string.digits)
    if special_var.get():
        password += random.choice(string.punctuation)

    # Fill the rest of the password with random characters from all categories
    for _ in range(length - len(password)):
        password += random.choice(characters)

    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))

    password_label.config(text="Generated Password: " + password)

# GUI setup
window = tk.Tk()
window.title("Password Generator")

length_label = tk.Label(window, text="Enter the desired length of the password:")
length_label.grid(row=0, column=0, padx=10, pady=5)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=5)

options_frame = tk.LabelFrame(window, text="Character Set Options")
options_frame.grid(row=1, columnspan=2, padx=10, pady=5, sticky="ew")

uppercase_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Uppercase Letters", variable=uppercase_var).grid(row=0, column=0, padx=5, pady=5, sticky="w")
lowercase_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Lowercase Letters", variable=lowercase_var).grid(row=1, column=0, padx=5, pady=5, sticky="w")
digits_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Digits", variable=digits_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")
special_var = tk.BooleanVar()
tk.Checkbutton(options_frame, text="Special Characters", variable=special_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)

password_label = tk.Label(window, text="")
password_label.grid(row=3, columnspan=2)

window.mainloop()
