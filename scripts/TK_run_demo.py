import tkinter as tk
from tkinter import Canvas, Button, Checkbutton

def next_step():
    print("Next Step")

def button2_click():
    print("Button 2 Clicked")

def button3_click():
    print("Button 3 Clicked")

def button4_click():
    print("Button 4 Clicked")

def button5_click():
    print("Button 5 Clicked")

def checkbox1_toggle():
    print("Checkbox 1 Toggled")

def checkbox2_toggle():
    print("Checkbox 2 Toggled")

def checkbox3_toggle():
    print("Checkbox 3 Toggled")

# Create the main window
root = tk.Tk()
root.title("Tkinter Interface")

# Create two figures (Canvas widgets)
figure1 = Canvas(root, width=200, height=200, bg="lightblue")
figure1.grid(row=0, column=0, padx=10, pady=10)

figure2 = Canvas(root, width=200, height=200, bg="lightgreen")
figure2.grid(row=0, column=1, padx=10, pady=10)

# Create buttons under the first figure
next_step = Button(root, text="Next Step", command=next_step)
next_step.grid(row=1, column=0, pady=5)

button2 = Button(root, text="Button 2", command=button2_click)
button2.grid(row=2, column=0, pady=5)

button3 = Button(root, text="Button 3", command=button3_click)
button3.grid(row=3, column=0, pady=5)

# Create buttons and checkboxes next to the second figure
button4 = Button(root, text="Button 4", command=button4_click)
button4.grid(row=1, column=1, pady=5)

button5 = Button(root, text="Button 5", command=button5_click)
button5.grid(row=2, column=1, pady=5)

checkbox1 = Checkbutton(root, text="Checkbox 1", command=checkbox1_toggle)
checkbox1.grid(row=3, column=1, pady=5)

checkbox2 = Checkbutton(root, text="Checkbox 2", command=checkbox2_toggle)
checkbox2.grid(row=4, column=1, pady=5)

checkbox3 = Checkbutton(root, text="Checkbox 3", command=checkbox3_toggle)
checkbox3.grid(row=5, column=1, pady=5)

# Start the Tkinter main loop
root.mainloop()
