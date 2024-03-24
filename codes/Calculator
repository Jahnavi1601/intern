from tkinter import *

strng = ""

def click(n):
    global strng
    strng = strng + str(n)
    eq.set(strng)

def equalto():
    try:
        global strng
        result = str(eval(strng))
        eq.set(result)
        strng = ""
    except:
        eq.set("Invalid")
        strng = ""

def clear():
    global strng
    strng = ""
    eq.set("")

def into():
    global strng
    if strng:
        strng2 = strng[:-1]
        exp_f.delete(0, END)
        exp_f.insert(0, strng2)
        strng = strng2

# Create the main application window
gui = Tk()
gui.configure(bg="black")
gui.title("Simple Calculator")

# Frame for the calculator
frame = Frame(gui, bg="black", padx=10, pady=10)
frame.grid(row=0, column=0)

# Setting up Entry and StringVar
eq = StringVar()
exp_f = Entry(frame, textvariable=eq, font=("Arial", 14), bd=5, insertwidth=4, width=10, bg="white", justify='right')
exp_f.grid(row=0, column=0, columnspan=4, pady=5)

# Button definitions
button_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'X'  # Adding "Clear" button
]

# Define buttons
buttons = []
for i, btn in enumerate(button_list):
    row = i // 4 + 1
    col = i % 4
    if btn.isdigit():
        buttons.append(Button(frame, text=btn, fg="black", bg="white", font=("Arial", 14), height=1, width=2, bd=3, command=lambda x=btn: click(x)))
    elif btn == '=':
        buttons.append(Button(frame, text=btn, fg="black", bg="orange", font=("Arial", 14), height=1, width=2, bd=3, command=equalto))
    elif btn == 'X':
        buttons.append(Button(frame, text=btn, fg="white", bg="red", font=("Arial", 14), height=1, width=2, bd=3, command=clear))
    else:
        buttons.append(Button(frame, text=btn, fg="white", bg="grey", font=("Arial", 14), height=1, width=2, bd=3, command=lambda x=btn: click(x)))

# Add buttons to grid with padding
for i, btn in enumerate(buttons):
    row = i // 4 + 2
    col = i % 4
    btn.grid(row=row, column=col, padx=5, pady=5)

# Binding the listbox to select_task function
gui.mainloop()
