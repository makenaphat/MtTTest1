import re
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


class RegexApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Text Analyzer with Regex (10 Functions)")
        self.root.geometry("900x650")
        self.create_widgets()

    def create_widgets(self):
        # --- Top Section: Load File & Parameters ---
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill=tk.X)

        ttk.Button(
            top_frame, text="📁 Load Text File", command=self.load_file
        ).grid(row=0, column=0, padx=5, pady=5)

        ttk.Label(top_frame, text="Pattern / Param:").grid(
            row=0, column=1, padx=5, pady=5
        )
        self.param_entry = ttk.Entry(top_frame, width=30)
        self.param_entry.insert(0, r"\d+")  # Default pattern (numbers)
        self.param_entry.grid(row=0, column=2, padx=5, pady=5)

        ttk.Label(top_frame, text="Replace Text:").grid(
            row=0, column=3, padx=5, pady=5
        )
        self.replace_entry = ttk.Entry(top_frame, width=20)
        self.replace_entry.insert(0, "[MASKED]")
        self.replace_entry.grid(row=0, column=4, padx=5, pady=5)

        # --- Text Input Area ---
        input_frame = ttk.LabelFrame(
            self.root, text=" Input Text ", padding=10
        )
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.input_text = tk.Text(input_frame, height=8)
        self.input_text.pack(fill=tk.BOTH, expand=True)

        # --- Action Buttons (10 Functions) ---
        btn_frame = ttk.LabelFrame(
            self.root, text=" re Module Functions ", padding=10
        )
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        functions = [
            ("1. findall", self.fn_findall),
            ("2. search", self.fn_search),
            ("3. match", self.fn_match),
            ("4. sub", self.fn_sub),
            ("5. subn", self.fn_subn),
            ("6. split", self.fn_split),
            ("7. finditer", self.fn_finditer),
            ("8. fullmatch", self.fn_fullmatch),
            ("9. compile & find", self.fn_compile),
            ("10. escape", self.fn_escape),
        ]

        row, col = 0, 0
        for name, func in functions:
            ttk.Button(btn_frame, text=name, command=func).grid(
                row=row, column=col, padx=4, pady=4, sticky="ew"
            )
            col += 1
            if col > 4:
                col = 0
                row += 1

        # --- Output Display Area ---
        output_frame = ttk.LabelFrame(
            self.root, text=" Result Output ", padding=10
        )
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.output_text = tk.Text(output_frame, height=8, bg="#f4f4f4")
        self.output_text.pack(fill=tk.BOTH, expand=True)

    def load_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror(
                    "Error Loading File", f"ไม่สามารถโหลดไฟล์ได้: {str(e)}"
                )

    def display_result(self, result):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, str(result))

    # --- 10 Regex Functions with try-except ---

    def fn_findall(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            res = re.findall(pattern, text)
            self.display_result(f"[findall]\nพบทั้งหมด {len(res)} รายการ:\n{res}")
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_search(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            match = re.search(pattern, text)
            if match:
                res = f"[search]\nพบตำแหน่งแรก: '{match.group()}' ที่ช่วง Index: {match.span()}"
            else:
                res = "[search]\nไม่พบข้อมูลที่ตรงตาม Pattern"
            self.display_result(res)
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_match(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            match = re.match(pattern, text)
            if match:
                res = f"[match]\nตรงกับจุดเริ่มต้นข้อความ: '{match.group()}'"
            else:
                res = "[match]\nจุดเริ่มต้นของข้อความไม่ตรงตาม Pattern"
            self.display_result(res)
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_sub(self):
        try:
            pattern = self.param_entry.get()
            repl = self.replace_entry.get()
            text = self.input_text.get("1.0", tk.END)
            res = re.sub(pattern, repl, text)
            self.display_result(f"[sub - เปลี่ยนข้อความ]:\n{res}")
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_subn(self):
        try:
            pattern = self.param_entry.get()
            repl = self.replace_entry.get()
            text = self.input_text.get("1.0", tk.END)
            new_text, count = re.subn(pattern, repl, text)
            self.display_result(
                f"[subn]\nจำนวนที่ถูกแทนที่: {count} จุด\n\nข้อความใหม่:\n{new_text}"
            )
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_split(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            res = re.split(pattern, text)
            self.display_result(
                f"[split]\nตัดแยกข้อความได้ {len(res)} ส่วน:\n{res}"
            )
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_finditer(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            matches = list(re.finditer(pattern, text))
            res = [
                f"Match: '{m.group()}' | Span: {m.span()}" for m in matches
            ]
            self.display_result(
                f"[finditer]\nพบทั้งหมด {len(res)} รายการ:\n"
                + "\n".join(res)
            )
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_fullmatch(self):
        try:
            pattern = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END).strip()
            match = re.fullmatch(pattern, text)
            if match:
                res = (
                    f"[fullmatch]\nข้อความทั้งหมดตรงตาม Pattern 100%: '{match.group()}'"
                )
            else:
                res = "[fullmatch]\nข้อความทั้งหมดไม่ได้ตรงตาม Pattern ทุกตัวอักษร"
            self.display_result(res)
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_compile(self):
        try:
            pattern_str = self.param_entry.get()
            text = self.input_text.get("1.0", tk.END)
            # คอมไพล์ regex พร้อม Flag IGNORECASE
            compiled_regex = re.compile(pattern_str, re.IGNORECASE)
            res = compiled_regex.findall(text)
            self.display_result(
                f"[compile + findall (Case-Insensitive)]\nผลลัพธ์:\n{res}"
            )
        except re.error as e:
            messagebox.showerror("Regex Error", f"Pattern ไม่ถูกต้อง: {e}")

    def fn_escape(self):
        try:
            pattern = self.param_entry.get()
            escaped = re.escape(pattern)
            self.display_result(
                f"[escape]\nข้อความต้นฉบับ: {pattern}\nข้อความหลังเติม Escape Characters:\n{escaped}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"เกิดข้อผิดพลาด: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = RegexApp(root)
    root.mainloop()