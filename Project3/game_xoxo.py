import tkinter as tk

class TicTacToeWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Tic-Tac-Toe (XO)")
        self.geometry("400x500")
        self.configure(bg="#1e1e2e")
        self.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.scores = {"X": 0, "O": 0}

        # Header
        self.label_status = tk.Label(
            self, 
            text="Turn: Player X", 
            font=("Consolas", 18, "bold"), 
            bg="#1e1e2e", 
            fg="#a6adc8"
        )
        self.label_status.pack(pady=15)

        # Board Frame
        frame_board = tk.Frame(self, bg="#181825")
        frame_board.pack(pady=10)

        self.buttons = []
        for i in range(9):
            btn = tk.Button(
                frame_board,
                text="",
                font=("Helvetica", 24, "bold"),
                width=4,
                height=2,
                bg="#313244",
                fg="#cdd6f4",
                activebackground="#45475a",
                bd=0,
                command=lambda idx=i: self.make_move(idx)
            )
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)

        # Score & Reset
        self.label_score = tk.Label(
            self, 
            text="Score - X: 0 | O: 0", 
            font=("Segoe UI", 12), 
            bg="#1e1e2e", 
            fg="#bac2de"
        )
        self.label_score.pack(pady=10)

        btn_reset = tk.Button(
            self, 
            text="Reset Game", 
            font=("Segoe UI", 11, "bold"), 
            bg="#f38ba8", 
            fg="#11111b", 
            activebackground="#f5e0dc",
            bd=0,
            padx=15, 
            pady=5, 
            command=self.reset_board
        )
        btn_reset.pack(pady=5)

    def make_move(self, idx):
        if self.board[idx] == "" and not self.check_winner():
            self.board[idx] = self.current_player
            color = "#89b4fa" if self.current_player == "X" else "#f9e2af"
            self.buttons[idx].config(text=self.current_player, fg=color)

            winner = self.check_winner()
            if winner:
                if winner == "Tie":
                    self.label_status.config(text="It's a Tie!", fg="#f9e2af")
                else:
                    self.label_status.config(text=f"Player {winner} Wins! 🎉", fg="#a6e3a1")
                    self.scores[winner] += 1
                    self.label_score.config(text=f"Score - X: {self.scores['X']} | O: {self.scores['O']}")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label_status.config(text=f"Turn: Player {self.current_player}")

    def check_winner(self):
        lines = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for a, b, c in lines:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                return self.board[a]
        if "" not in self.board:
            return "Tie"
        return None

    def reset_board(self):
        self.board = [""] * 9
        self.current_player = "X"
        self.label_status.config(text="Turn: Player X", fg="#a6adc8")
        for btn in self.buttons:
            btn.config(text="", bg="#313244")