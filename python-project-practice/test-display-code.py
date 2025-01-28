import tkinter as tk
import time

def county(wait, label):
    while wait != 0:
        label.config(text=str(wait))  # Update the label with the current countdown value
        wait -= 1
        time.sleep(1)
        window.update()  # Update the window with the new label value
    label.config(text="Time's up!")  # When the countdown reaches 0, display "Time's up!"

# Set up the main window
window = tk.Tk()
window.title("Countdown Timer")

# Create a label to display the countdown
label = tk.Label(window, font=("Helvetica", 48), fg="red")
label.pack()

# Input field for the number of seconds
userinput = int(input("Enter number of seconds: "))

# Start the countdown with the input number of seconds
county(userinput, label)

# Run the Tkinter event loop
window.mainloop()
