import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
user_score = 0
comp_score = 0

def play(user_choice):
    global user_score, comp_score
    
    computer_choice = random.choice(choices)
    result_text = ""

    if user_choice == computer_choice:
        result_text = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_text = "✅ You Win!"
        user_score += 1
    else:
        result_text = "❌ You Lose!"
        comp_score += 1
    
    user_choice_label.config(text=f"Your Choice: {user_choice}")
    comp_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=result_text)
    score_label.config(text=f"Score: You {user_score} - {comp_score} Computer")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    user_choice_label.config(text="Your Choice: ")
    comp_choice_label.config(text="Computer's Choice: ")
    result_label.config(text="")
    score_label.config(text="Score: You 0 - 0 Computer")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x400")
root.configure(bg="#222")

tk.Label(root, text="🎮 Rock - Paper - Scissors 🎮", font=("Arial", 18, "bold"), bg="#222", fg="white").pack(pady=10)

user_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14), bg="#222", fg="white")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14), bg="#222", fg="white")
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#222", fg="yellow")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: You 0 - 0 Computer", font=("Arial", 14), bg="#222", fg="white")
score_label.pack(pady=5)

button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=20)

tk.Button(button_frame, text="Rock", width=10, font=("Arial", 14), bg="#444", fg="white",
          command=lambda: play("Rock")).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text="Paper", width=10, font=("Arial", 14), bg="#444", fg="white",
          command=lambda: play("Paper")).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 14), bg="#444", fg="white",
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=10)

tk.Button(root, text="🔄 Reset Game", width=15, font=("Arial", 12), bg="#BB3E03", fg="white",
          command=reset_game).pack(pady=15)

root.mainloop()
