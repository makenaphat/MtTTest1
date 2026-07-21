import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Snake Game Classic")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # ตั้งค่าเกม
        self.GAME_WIDTH = 400
        self.GAME_HEIGHT = 400
        self.SPEED = 100
        self.SPACE_SIZE = 20
        self.BODY_PARTS = 3

        self.score = 0
        self.high_score = 0
        self.direction = 'down'
        self.running = False

        # Header คะแนน
        self.frame_score = tk.Frame(root, bg="#1e1e2e")
        self.frame_score.pack(pady=10)

        self.label_score = tk.Label(
            self.frame_score, 
            text="Score: 0  |  High Score: 0", 
            font=("Segoe UI", 14, "bold"), 
            bg="#1e1e2e", 
            fg="#a6e3a1"
        )
        self.label_score.pack()

        # Canvas พื้นที่เล่นเกม
        self.canvas = tk.Canvas(
            root, 
            bg="#181825", 
            height=self.GAME_HEIGHT, 
            width=self.GAME_WIDTH, 
            highlightthickness=2, 
            highlightbackground="#45475a"
        )
        self.canvas.pack()

        # ข้อความแนะนำ
        self.label_msg = tk.Label(
            root, 
            text="Press [SPACE] to Start / Restart", 
            font=("Segoe UI", 11), 
            bg="#1e1e2e", 
            fg="#f9e2af"
        )
        self.label_msg.pack(pady=15)

        # ปุ่มควบคุม
        self.root.bind("<Left>", lambda event: self.change_direction('left'))
        self.root.bind("<Right>", lambda event: self.change_direction('right'))
        self.root.bind("<Up>", lambda event: self.change_direction('up'))
        self.root.bind("<Down>", lambda event: self.change_direction('down'))
        self.root.bind("<space>", lambda event: self.start_game())

    def start_game(self):
        if self.running:
            return

        self.canvas.delete("all")
        self.score = 0
        self.direction = 'down'
        self.running = True
        self.label_score.config(text=f"Score: {self.score}  |  High Score: {self.high_score}")
        self.label_msg.config(text="Use Arrow Keys (⬆️⬇️⬅️➡️) to Move", fg="#a6adc8")

        self.snake_coordinates = []
        for i in range(0, self.BODY_PARTS):
            self.snake_coordinates.append([0, 0])

        self.snake_squares = []
        for x, y in self.snake_coordinates:
            square = self.canvas.create_rectangle(
                x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, 
                fill="#89b4fa", outline="#11111b"
            )
            self.snake_squares.append(square)

        self.spawn_food()
        self.next_turn()

    def spawn_food(self):
        x = random.randint(0, (self.GAME_WIDTH // self.SPACE_SIZE) - 1) * self.SPACE_SIZE
        y = random.randint(0, (self.GAME_HEIGHT // self.SPACE_SIZE) - 1) * self.SPACE_SIZE
        self.food_coord = [x, y]

        self.canvas.create_oval(
            x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, 
            fill="#f38ba8", tag="food", outline="#11111b"
        )

    def next_turn(self):
        if not self.running:
            return

        x, y = self.snake_coordinates[0]

        if self.direction == "up":
            y -= self.SPACE_SIZE
        elif self.direction == "down":
            y += self.SPACE_SIZE
        elif self.direction == "left":
            x -= self.SPACE_SIZE
        elif self.direction == "right":
            x += self.SPACE_SIZE

        self.snake_coordinates.insert(0, (x, y))
        square = self.canvas.create_rectangle(
            x, y, x + self.SPACE_SIZE, y + self.SPACE_SIZE, 
            fill="#89b4fa", outline="#11111b"
        )
        self.snake_squares.insert(0, square)

        if x == self.food_coord[0] and y == self.food_coord[1]:
            self.score += 1
            if self.score > self.high_score:
                self.high_score = self.score
            self.label_score.config(text=f"Score: {self.score}  |  High Score: {self.high_score}")
            self.canvas.delete("food")
            self.spawn_food()
        else:
            del self.snake_coordinates[-1]
            self.canvas.delete(self.snake_squares[-1])
            del self.snake_squares[-1]

        if self.check_collisions():
            self.game_over()
        else:
            self.root.after(self.SPEED, self.next_turn)

    def change_direction(self, new_dir):
        if new_dir == 'left' and self.direction != 'right':
            self.direction = new_dir
        elif new_dir == 'right' and self.direction != 'left':
            self.direction = new_dir
        elif new_dir == 'up' and self.direction != 'down':
            self.direction = new_dir
        elif new_dir == 'down' and self.direction != 'up':
            self.direction = new_dir

    def check_collisions(self):
        x, y = self.snake_coordinates[0]

        if x < 0 or x >= self.GAME_WIDTH or y < 0 or y >= self.GAME_HEIGHT:
            return True

        for body_part in self.snake_coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True

        return False

    def game_over(self):
        self.running = False
        self.canvas.delete("all")
        self.canvas.create_text(
            self.GAME_WIDTH/2, self.GAME_HEIGHT/2 - 20,
            font=('Segoe UI', 30, 'bold'), text="GAME OVER", fill="#f38ba8"
        )
        self.canvas.create_text(
            self.GAME_WIDTH/2, self.GAME_HEIGHT/2 + 20,
            font=('Segoe UI', 14), text=f"Final Score: {self.score}", fill="#cdd6f4"
        )
        self.label_msg.config(text="Press [SPACE] to Play Again!", fg="#f9e2af")