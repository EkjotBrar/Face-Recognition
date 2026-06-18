import tkinter as tk
from tkinter import messagebox

def create_button(window, text, color, command, fg='white'):
    button = tk.Button(
        window,
        text=text,
        activebackground="dark green",
        activeforeground="white",
        bg=color,
        fg=fg,
        command=command,
        height=2,
        width=20,
        font=('Times New Roman', 20, 'bold')
    )
    return button

def get_img_label(window):
    label = tk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = tk.Label(
        window,
        text=text)
    label.config(font=('Times New Roman', 20, 'bold'), justify='left')
    return label

def get_entry_text(window):
    input_txt = tk.Text(window, height=2, width=15, font=("Arial", 32))

    return input_txt

def msg_box(title, message):
    messagebox.showinfo(title, message)