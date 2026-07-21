import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Number Guessing Game")
        self.geometry("400x450")
        self.configure(bg="#1e1e2e")
        self.resizable(False, False)

        self.target = random.randint(1, 100)
        self.attempts = 0

        tk.Label(
            self, 
            text="Guess The Number!", 
            font=("Segoe UI", 20, "bold"), 
            bg="#1e1e2e", 
            fg="#cdd6f4"
        ).pack(pady=15)

        tk.Label(
            self, 
            text="I'm thinking of a number between 1 and 100", 
            font=("Segoe UI", 11), 
            bg="#1e1e2e", 
            fg="#a6adc8"
        ).pack(pady=5)

        self.entry = tk.Entry(
            self, 
            font=("Consolas", 18, "bold"), 
            justify="center", 
            bg="#313244", 
            fg="#a6e3a1", 
            insertbackground="white",
            bd=0
        )
        self.entry.pack(pady=15, ipady=8)
        self.entry.bind("<Return>", lambda e: self.check_guess())

        btn_guess = tk.Button(
            self, 
            text="Submit Guess", 
            font=("Segoe UI", 12, "bold"), 
            bg="#a6e3a1", 
            fg="#11111b", 
            activebackground="#94e2d5",
            bd=0,
            padx=20, 
            pady=8, 
            command=self.check_guess
        )
        btn_guess.pack(pady=10)

        self.label_hint = tk.Label(
            self, 
            text="Enter a number to start!", 
            font=("Segoe UI", 12), 
            bg="#1e1e2e", 
            fg="#f9e2af"
        )
        self.label_hint.pack(pady=10)

        self.label_attempts = tk.Label(
            self, 
            text="Attempts: 0", 
            font=("Segoe UI", 10), 
            bg="#1e1e2e", 
            fg="#bac2de"
        )
        self.label_attempts.pack(pady=5)

    def check_guess(self):
        val = self.entry.get().strip()
        if not val.isdigit():
            messagebox.showwarning("Warning", "Please enter a valid number!")
            return

        guess = int(val)
        self.attempts += 1
        self.label_attempts.config(text=f"Attempts: {self.attempts}")
        self.entry.delete(0, tk.END)

        if guess < self.target:
            self.label_hint.config(text="📈 Too Low! Try higher.", fg="#89b4fa")
        elif guess > self.target:
            self.label_hint.config(text="📉 Too High! Try lower.", fg="#f38ba8")
        else:
            self.label_hint.config(text=f"🎉 Correct! The number was {self.target}", fg="#a6e3a1")
            messagebox.showinfo("Victory!", f"You guessed it in {self.attempts} attempts!")
            self.reset_game()

    def reset_game(self):
        self.target = random.randint(1, 100)
        self.attempts = 0
        self.label_attempts.config(text="Attempts: 0")
        self.label_hint.config(text="New game started! Guess a number.", fg="#f9e2af")