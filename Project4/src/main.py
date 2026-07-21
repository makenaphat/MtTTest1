import tkinter as tk
from game_snake import SnakeGame

def main():
    root = tk.Tk()
    # เรียกเปิดเกมทันทีโดยไม่ต้องผ่านหน้าเมนู
    app = SnakeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()