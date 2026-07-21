import tkinter as tk

# ดึง (Import) หน้าต่างเกมจากไฟล์เกมแยกทั้ง 2 ไฟล์
from game_xoxo import TicTacToeWindow
from game_guessing import NumberGuessingWindow

def main():
    root = tk.Tk()
    root.title("Game Launcher")
    root.geometry("450x400")
    root.configure(bg="#181825")
    root.resizable(False, False)

    # Header Title
    tk.Label(
        root, 
        text="🎮 GAME CENTER", 
        font=("Impact", 28), 
        bg="#181825", 
        fg="#cba6f7"
    ).pack(pady=(30, 5))

    tk.Label(
        root, 
        text="Choose a game to play:", 
        font=("Segoe UI", 12), 
        bg="#181825", 
        fg="#a6adc8"
    ).pack(pady=(0, 25))

    # Button: Launch Game 1
    btn_game1 = tk.Button(
        root,
        text="❌  Tic-Tac-Toe (XO)  ⭕",
        font=("Segoe UI", 14, "bold"),
        bg="#89b4fa",
        fg="#11111b",
        activebackground="#b4befe",
        bd=0,
        pady=12,
        cursor="hand2",
        command=lambda: TicTacToeWindow(root)
    )
    btn_game1.pack(fill="x", padx=50, pady=10)

    # Button: Launch Game 2
    btn_game2 = tk.Button(
        root,
        text="🎯  Number Guessing Game  🎲",
        font=("Segoe UI", 14, "bold"),
        bg="#a6e3a1",
        fg="#11111b",
        activebackground="#94e2d5",
        bd=0,
        pady=12,
        cursor="hand2",
        command=lambda: NumberGuessingWindow(root)
    )
    btn_game2.pack(fill="x", padx=50, pady=10)

    # Footer
    tk.Label(
        root, 
        text="Powered by Python Tkinter", 
        font=("Consolas", 9), 
        bg="#181825", 
        fg="#585b70"
    ).pack(side="bottom", pady=15)

    root.mainloop()

# เรียกใช้งานฟังก์ชัน main เมื่อกดรันไฟล์นี้
if __name__ == "__main__":
    main()