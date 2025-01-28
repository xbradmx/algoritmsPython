import tkinter as tk
import random

def play_game(player_choice, label_result):
    # List of possible choices
    choices = ["Rock", "Paper", "Scissors"]
    # Computer's choice
    computer_choice = random.choice(choices)
    
    # Determine the winner
    if player_choice == computer_choice:
        result = f"It's a tie! Computer chose {computer_choice}."
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = f"You win! Computer chose {computer_choice}."
    else:
        result = f"You lose! Computer chose {computer_choice}."
    
    # Display the result
    label_result.config(text=result)

# Set up the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors")

# Label for displaying the result
label_result = tk.Label(window, font=("Helvetica", 16), fg="blue", height=4)
label_result.pack(pady=20)

# Title Label
label_title = tk.Label(window, text="Choose your move!", font=("Helvetica", 18))
label_title.pack(pady=10)

# Buttons for player's choices
btn_rock = tk.Button(window, text="Rock", font=("Helvetica", 14), width=10, height=2, 
                     command=lambda: play_game("Rock", label_result))
btn_rock.pack(side=tk.LEFT, padx=20, pady=20)

btn_paper = tk.Button(window, text="Paper", font=("Helvetica", 14), width=10, height=2, 
                      command=lambda: play_game("Paper", label_result))
btn_paper.pack(side=tk.LEFT, padx=20, pady=20)

btn_scissors = tk.Button(window, text="Scissors", font=("Helvetica", 14), width=10, height=2, 
                         command=lambda: play_game("Scissors", label_result))
btn_scissors.pack(side=tk.LEFT, padx=20, pady=20)

# Run the Tkinter event loop
window.mainloop()
