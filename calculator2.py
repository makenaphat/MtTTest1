import customtkinter as ctk

# Set up the overall theme and color of the program
ctk.set_appearance_mode("System")  # Automatically matches Windows Light/Dark mode
ctk.set_default_color_theme("blue")

class ModernCalculator(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window configuration
        self.title("Modern Calculator")
        self.geometry("360x520")
        self.resizable(False, False) # Lock window size for a consistent layout

        self.current_value = ""

        # --- Display Screen ---
        self.display = ctk.CTkLabel(
            self, 
            text="0", 
            anchor="e", 
            font=("Helvetica", 40, "bold"),
            padx=20
        )
        self.display.pack(expand=True, fill="both", padx=20, pady=(20, 10))

        # --- Buttons Frame ---
        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(expand=True, fill="both", padx=20, pady=(0, 20))

        # Configure Grid Rows and Columns
        self.buttons_frame.rowconfigure((0,1,2,3,4), weight=1, pad=8)
        self.buttons_frame.columnconfigure((0,1,2,3), weight=1, pad=8)

        # Button Layout Configuration: (Text, Row, Column, fg_color, hover_color)
        button_config = [
            ('C', 0, 0, "#FF4B4B", "#FF3333"), ('(', 0, 1, None, None), (')', 0, 2, None, None), ('/', 0, 3, "#FF9500", "#E68600"),
            ('7', 1, 0, None, None), ('8', 1, 1, None, None), ('9', 1, 2, None, None), ('*', 1, 3, "#FF9500", "#E68600"),
            ('4', 2, 0, None, None), ('5', 2, 1, None, None), ('6', 2, 2, None, None), ('-', 2, 3, "#FF9500", "#E68600"),
            ('1', 3, 0, None, None), ('2', 3, 1, None, None), ('3', 3, 2, None, None), ('+', 3, 3, "#FF9500", "#E68600"),
            ('0', 4, 0, None, None), ('.', 4, 1, None, None), ('⌫', 4, 2, None, None), ('=', 4, 3, "#2CC990", "#27B280")
        ]

        # Render buttons onto the window
        for text, row, col, fg_color, hover_color in button_config:
            # If it's a regular number/bracket, use a sleek Adaptive theme color
            if fg_color is None:
                fg_color = ("#EAEAEA", "#2B2B2B") # (Light Mode Color, Dark Mode Color)
                hover_color = ("#D5D5D5", "#3A3A3A")
                text_color = ("#000000", "#FFFFFF")
            else:
                text_color = "#FFFFFF"

            btn = ctk.CTkButton(
                self.buttons_frame, 
                text=text,
                font=("Helvetica", 20, "bold"),
                fg_color=fg_color,
                hover_color=hover_color,
                text_color=text_color,
                corner_radius=15, # Smooth rounded corners
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=4, pady=4)

    # Click Event Logic
    def on_button_click(self, char):
        if char == 'C':
            self.current_value = ""
        elif char == '⌫':
            self.current_value = self.current_value[:-1]
        elif char == '=':
            try:
                if self.current_value:
                    # Evaluate the mathematical string expression safely
                    result = str(eval(self.current_value))
                    # Clean up trailing decimals if it's a whole number (e.g., 5.0 -> 5)
                    if result.endswith('.0'):
                        result = result[:-2]
                    self.current_value = result
            except ZeroDivisionError:
                self.current_value = "Error (Div by 0)"
            except Exception:
                self.current_value = "Error"
        else:
            self.current_value += str(char)

        # Update display screen text
        if self.current_value == "":
            self.display.configure(text="0")
        else:
            self.display.configure(text=self.current_value)

if __name__ == "__main__":
    app = ModernCalculator()
    app.mainloop()