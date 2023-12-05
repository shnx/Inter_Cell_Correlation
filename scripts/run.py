import tkinter as tk
from tkinter import Canvas, Button, Checkbutton

def next_step():
    print("Next Step")


# Create the main window
root = tk.Tk()
root.title("Tkinter Interface")

# Create two figures (Canvas widgets)
figure1 = Canvas(root, width=400, height=400, bg="lightblue")
figure1.grid(row=0, column=0, padx=10, pady=10)

figure2 = Canvas(root, width=400, height=400, bg="lightgreen")
figure2.grid(row=0, column=1, padx=10, pady=10)

# Create buttons under the first figure
next_step = Button(root, text="Next Step", command=next_step)
next_step.grid(row=1, column=0, pady=20)


# Start the Tkinter main loop
root.mainloop()
