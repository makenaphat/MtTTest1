import re
import tkinter as tk
from tkinter import messagebox, ttk


class StringProcessorGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Text & String Processor Utility")
        self.root.geometry("800x600")

        # Layout Main Frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Input Section
        lbl_input = ttk.Label(
            main_frame, text="ข้อความต้นฉบับ (Input Text):", font=("Helvetica", 10, "bold")
        )
        lbl_input.pack(anchor=tk.W, pady=(0, 2))

        self.txt_input = tk.Text(main_frame, height=8, font=("Consolas", 10))
        self.txt_input.pack(fill=tk.X, pady=(0, 10))
        self.txt_input.insert(
            tk.END, "Hello World! Welcome to Python Programming. Contact: test@example.com, 081-234-5678"
        )

        # Controls Section
        control_frame = ttk.LabelFrame(
            main_frame, text=" ฟังก์ชันและตัวเลือกการทำงาน ", padding="10"
        )
        control_frame.pack(fill=tk.X, pady=(0, 10))

        # Inputs for Find/Replace/Regex
        grid_frame = ttk.Frame(control_frame)
        grid_frame.pack(fill=tk.X, pady=(0, 5))

        ttk.Label(grid_frame, text="ค้นหา (Search Target):").grid(
            row=0, column=0, sticky=tk.W, padx=2
        )
        self.ent_target = ttk.Entry(grid_frame, width=25)
        self.ent_target.grid(row=0, column=1, padx=5, pady=2)

        ttk.Label(grid_frame, text="แทนที่ด้วย (Replace With):").grid(
            row=0, column=2, sticky=tk.W, padx=2
        )
        self.ent_replace = ttk.Entry(grid_frame, width=25)
        self.ent_replace.grid(row=0, column=3, padx=5, pady=2)

        # Buttons Grid (10+ String Functions)
        btn_frame = ttk.Frame(control_frame)
        btn_frame.pack(fill=tk.X, pady=5)

        # Row 1: Search & Format
        ttk.Button(
            btn_frame, text="1. ค้นหาตำแหน่ง (Find Position)", command=self.fn_find_pos
        ).grid(row=0, column=0, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame, text="2. นับจำนวนคำที่พบ (Count Words)", command=self.fn_count_word
        ).grid(row=0, column=1, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame,
            text="3. ค้นหาด้วย Regex (Regex Find)",
            command=self.fn_regex_find,
        ).grid(row=0, column=2, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame, text="4. ค้นหาและแทนที่ (Replace)", command=self.fn_replace
        ).grid(row=0, column=3, padx=3, pady=3, sticky="ew")

        # Row 2: Transform Case
        ttk.Button(
            btn_frame, text="5. ตัวพิมพ์ใหญ่ (UPPERCASE)", command=self.fn_uppercase
        ).grid(row=1, column=0, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame, text="6. ตัวพิมพ์เล็ก (lowercase)", command=self.fn_lowercase
        ).grid(row=1, column=1, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame, text="7. ตัวใหญ่หน้าคำ (Title Case)", command=self.fn_titlecase
        ).grid(row=1, column=2, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame, text="8. สลับตัวพิมพ์ (sWAP cASE)", command=self.fn_swapcase
        ).grid(row=1, column=3, padx=3, pady=3, sticky="ew")

        # Row 3: Clean & Utility
        ttk.Button(
            btn_frame,
            text="9. ตัดช่องว่างหัว/ท้าย (Trim Spaces)",
            command=self.fn_trim,
        ).grid(row=2, column=0, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame,
            text="10. กลับอักขระ (Reverse String)",
            command=self.fn_reverse,
        ).grid(row=2, column=1, padx=3, pady=3, sticky="ew")
        ttk.Button(
            btn_frame,
            text="11. สถิติจำนวนคำ/ตัวอักษร (Word Count)",
            command=self.fn_stats,
        ).grid(row=2, column=2, padx=3, pady=3, sticky="ew")

        for col in range(4):
            btn_frame.columnconfigure(col, weight=1)

        # Output Section
        lbl_output = ttk.Label(
            main_frame, text="ผลลัพธ์ (Output Result):", font=("Helvetica", 10, "bold")
        )
        lbl_output.pack(anchor=tk.W, pady=(5, 2))

        self.txt_output = tk.Text(main_frame, height=10, font=("Consolas", 10))
        self.txt_output.pack(fill=tk.BOTH, expand=True)

    # --- Utility Methods ---
    def get_input(self):
        return self.txt_input.get("1.0", tk.END).rstrip("\n")

    def set_output(self, text):
        self.txt_output.delete("1.0", tk.END)
        self.txt_output.insert(tk.END, text)

    # --- String Functions Implementation ---

    # 1. Search Position
    def fn_find_pos(self):
        text = self.get_input()
        target = self.ent_target.get()
        if not target:
            messagebox.showwarning(
                "คำเตือน", "กรุณากรอกคำที่ต้องการค้นหาในช่อง Search Target"
            )
            return
        pos = text.find(target)
        if pos != -1:
            self.set_output(
                f"พบคำว่า '{target}' ที่ Index ตำแหน่งแรกคือ: {pos}\n(นับรวมช่องว่างและอักขระ)"
            )
        else:
            self.set_output(f"ไม่พบคำว่า '{target}' ในข้อความ")

    # 2. Count Occurrences
    def fn_count_word(self):
        text = self.get_input()
        target = self.ent_target.get()
        if not target:
            messagebox.showwarning("คำเตือน", "กรุณากรอกคำที่ต้องการนับในช่อง Search Target")
            return
        count = text.count(target)
        self.set_output(f"พบคำว่า '{target}' ทั้งหมดจำนวน: {count} ครั้ง")

    # 3. Regex Find
    def fn_regex_find(self):
        text = self.get_input()
        pattern = self.ent_target.get()
        if not pattern:
            messagebox.showwarning(
                "คำเตือน", "กรุณากรอก Regex Pattern ในช่อง Search Target\n(เช่น \\d+ หรือ [a-z]+)"
            )
            return
        try:
            matches = re.findall(pattern, text)
            result = f"การค้นหาด้วย Regex รูปแบบ: {pattern}\n"
            result += f"จำนวนที่พบ: {len(matches)} รายการ\n"
            result += "รายการที่พบ: " + ", ".join(map(str, matches))
            self.set_output(result)
        except re.error as e:
            messagebox.showerror("Error", f"Pattern ไม่ถูกต้อง: {e}")

    # 4. Find & Replace
    def fn_replace(self):
        text = self.get_input()
        target = self.ent_target.get()
        replace_with = self.ent_replace.get()
        if not target:
            messagebox.showwarning(
                "คำเตือน", "กรุณากรอกคำที่ต้องการแทนที่ในช่อง Search Target"
            )
            return
        result = text.replace(target, replace_with)
        self.set_output(result)

    # 5. Uppercase
    def fn_uppercase(self):
        self.set_output(self.get_input().upper())

    # 6. Lowercase
    def fn_lowercase(self):
        self.set_output(self.get_input().lower())

    # 7. Title Case
    def fn_titlecase(self):
        self.set_output(self.get_input().title())

    # 8. Swap Case
    def fn_swapcase(self):
        self.set_output(self.get_input().swapcase())

    # 9. Trim / Strip
    def fn_trim(self):
        self.set_output(self.get_input().strip())

    # 10. Reverse String
    def fn_reverse(self):
        self.set_output(self.get_input()[::-1])

    # 11. Word & Character Statistics
    def fn_stats(self):
        text = self.get_input()
        char_count = len(text)
        char_no_space = len(text.replace(" ", ""))
        words = text.split()
        word_count = len(words)
        lines = text.splitlines()
        line_count = len(lines)

        result = (
            f"=== สถิติของข้อความ ===\n"
            f"- จำนวนตัวอักษรทั้งหมด (รวมช่องว่าง): {char_count}\n"
            f"- จำนวนตัวอักษร (ไม่รวมช่องว่าง): {char_no_space}\n"
            f"- จำนวนคำ: {word_count}\n"
            f"- จำนวนบรรทัด: {line_count}"
        )
        self.set_output(result)


if __name__ == "__main__":
    root = tk.Tk()
    app = StringProcessorGUI(root)
    root.mainloop()
