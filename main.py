import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    entry.delete(0, tk.END)
    entry.insert(0, password)

def copy_to_clipboard():
    password = entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy.")

# Window setup
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x300")
root.configure(bg="#F9F9F9")  # Light gray background

# Fonts
main_font = ("Segoe UI", 12)
heading_font = ("Segoe UI", 14, "bold")

# Password length input
length_label = tk.Label(root, text="Enter password length:", font=main_font, bg="#F9F9F9")
length_label.pack(pady=5)

length_entry = tk.Entry(root, width=10, font=main_font, justify='center')
length_entry.pack(pady=5)
length_entry.insert(0, "12")

# Generate button (shifted up!)
button = tk.Button(root, text="Generate Password", command=generate_password,
                   font=main_font, bg="#E6E6FA", fg="black")
button.pack(pady=10)

# Password label (optional heading)
label = tk.Label(root, text="Your password:", font=heading_font, bg="#F9F9F9")
label.pack(pady=5)

# Output password field
entry = tk.Entry(root, width=30, font=main_font, justify='center')
entry.pack(pady=5)

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy Password", command=copy_to_clipboard,
                        font=main_font, bg="#E6E6FA", fg="black")
copy_button.pack(pady=10)

# Run the app
root.mainloop()
