import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import random
import csv

class GradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ระบบตัดเกรดวิชา Basic Computer Programming (20 คน)")
        self.root.geometry("850x650")
        self.root.resizable(True, True)

        # ข้อมูลนักศึกษา
        self.students = []

        self.setup_ui()

    def setup_ui(self):
        # --- Header ---
        header_frame = ttk.Frame(self.root, padding=10)
        header_frame.pack(fill=tk.X)
        
        ttk.Label(
            header_frame, 
            text="โปรแกรมรวมคะแนนและตัดเกรดวิชา Basic Computer Programming", 
            font=("Helvetica", 14, "bold")
        ).pack()

        # --- Input Frame ---
        input_frame = ttk.LabelFrame(self.root, text=" เพิ่ม / แก้ไข ข้อมูลนักศึกษา ", padding=10)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(input_frame, text="รหัสนักศึกษา:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.ent_id = ttk.Entry(input_frame, width=15)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="ชื่อ-นามสกุล:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.E)
        self.ent_name = ttk.Entry(input_frame, width=20)
        self.ent_name.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(input_frame, text="Midterm (50):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        self.ent_midterm = ttk.Entry(input_frame, width=15)
        self.ent_midterm.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Final (50):").grid(row=1, column=2, padx=5, pady=5, sticky=tk.E)
        self.ent_final = ttk.Entry(input_frame, width=20)
        self.ent_final.grid(row=1, column=3, padx=5, pady=5)

        # Buttons in Input Frame
        btn_add = ttk.Button(input_frame, text="เพิ่มข้อมูล", command=self.add_student)
        btn_add.grid(row=0, column=4, rowspan=2, padx=10, pady=5, sticky=tk.NSEW)

        btn_generate = ttk.Button(input_frame, text="สุ่มตัวอย่าง 20 คน", command=self.generate_sample_20)
        btn_generate.grid(row=0, column=5, rowspan=2, padx=5, pady=5, sticky=tk.NSEW)

        # --- Table Frame (Treeview) ---
        table_frame = ttk.Frame(self.root, padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("id", "name", "midterm", "final", "total", "grade")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=12)
        
        self.tree.heading("id", text="รหัสนักศึกษา")
        self.tree.heading("name", text="ชื่อ-นามสกุล")
        self.tree.heading("midterm", text="Midterm (50)")
        self.tree.heading("final", text="Final (50)")
        self.tree.heading("total", text="คะแนนรวม (100)")
        self.tree.heading("grade", text="เกรด")

        self.tree.column("id", width=110, anchor=tk.CENTER)
        self.tree.column("name", width=200, anchor=tk.W)
        self.tree.column("midterm", width=100, anchor=tk.CENTER)
        self.tree.column("final", width=100, anchor=tk.CENTER)
        self.tree.column("total", width=110, anchor=tk.CENTER)
        self.tree.column("grade", width=80, anchor=tk.CENTER)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # --- Summary & Actions Frame ---
        bottom_frame = ttk.LabelFrame(self.root, text=" สรุปผลและฟังก์ชัน ", padding=10)
        bottom_frame.pack(fill=tk.X, padx=10, pady=5)

        self.lbl_summary = ttk.Label(bottom_frame, text="จำนวนนักศึกษา: 0 คน | คะแนนเฉลี่ย: 0.0 | ผ่าน (A-D): 0 คน | ตก (F): 0 คน", font=("Helvetica", 10, "bold"))
        self.lbl_summary.pack(side=tk.LEFT, padx=5)

        btn_export = ttk.Button(bottom_frame, text="ส่งออกไฟล์ CSV", command=self.export_csv)
        btn_export.pack(side=tk.RIGHT, padx=5)

        btn_clear = ttk.Button(bottom_frame, text="ล้างข้อมูลทั้งหมด", command=self.clear_all)
        btn_clear.pack(side=tk.RIGHT, padx=5)

    def calculate_grade(self, total):
        """เกณฑ์การตัดเกรดอิงกลุ่ม/อิงเกณฑ์มาตรฐาน"""
        if total >= 80: return "A"
        elif total >= 75: return "B+"
        elif total >= 70: return "B"
        elif total >= 65: return "C+"
        elif total >= 60: return "C"
        elif total >= 55: return "D+"
        elif total >= 50: return "D"
        else: return "F"

    def add_student(self):
        s_id = self.ent_id.get().strip()
        name = self.ent_name.get().strip()
        
        try:
            midterm = float(self.ent_midterm.get())
            final = float(self.ent_final.get())

            if not s_id or not name:
                messagebox.showwarning("แจ้งเตือน", "กรุณากรอกรหัสและชื่อนักศึกษา")
                return
            
            if not (0 <= midterm <= 50) or not (0 <= final <= 50):
                messagebox.showwarning("แจ้งเตือน", "คะแนน Midterm และ Final ต้องอยู่ระหว่าง 0 - 50 คะแนน")
                return

            total = midterm + final
            grade = self.calculate_grade(total)

            student_data = {
                "id": s_id,
                "name": name,
                "midterm": midterm,
                "final": final,
                "total": total,
                "grade": grade
            }

            self.students.append(student_data)
            self.refresh_table()

            # Clear inputs
            self.ent_id.delete(0, tk.END)
            self.ent_name.delete(0, tk.END)
            self.ent_midterm.delete(0, tk.END)
            self.ent_final.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกคะแนนเป็นตัวเลข")

    def generate_sample_20(self):
        """สร้างข้อมูลนักศึกษา 20 คนแบบอัตโนมัติ"""
        first_names = ["สมชาย", "วิภา", "กิตติ", "อนันต์", "ปรียา", "นพดล", "ศิริพร", "ชัยวัฒน์", "รัตนา", "ธีรพงษ์"]
        last_names = ["ใจดี", "มีสุข", "มั่นคง", "เจริญ", "วงค์สุวรรณ", "บุญมี", "สุขสันต์", "คงกระพัน"]

        self.students.clear()
        for i in range(1, 21):
            s_id = f"670100{i:02d}"
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            midterm = round(random.uniform(20.0, 48.0), 1)
            final = round(random.uniform(15.0, 49.0), 1)
            total = round(midterm + final, 1)
            grade = self.calculate_grade(total)

            self.students.append({
                "id": s_id,
                "name": name,
                "midterm": midterm,
                "final": final,
                "total": total,
                "grade": grade
            })

        self.refresh_table()
        messagebox.showinfo("สำเร็จ", "เพิ่มข้อมูลสุ่มนักศึกษา 20 คน เรียบร้อยแล้ว!")

    def refresh_table(self):
        # ล้างข้อมูลในตารางเก่า
        for item in self.tree.get_children():
            self.tree.delete(item)

        # ใส่ข้อมูลใหม่
        total_score_sum = 0
        pass_count = 0
        fail_count = 0

        for s in self.students:
            self.tree.insert("", tk.END, values=(s["id"], s["name"], s["midterm"], s["final"], s["total"], s["grade"]))
            total_score_sum += s["total"]
            if s["grade"] == "F":
                fail_count += 1
            else:
                pass_count += 1

        # อัปเดตสถิติ
        total_students = len(self.students)
        avg_score = (total_score_sum / total_students) if total_students > 0 else 0.0
        
        self.lbl_summary.config(
            text=f"จำนวนนักศึกษา: {total_students} คน | คะแนนเฉลี่ย: {avg_score:.2f} | ผ่าน: {pass_count} คน | ตก (F): {fail_count} คน"
        )

    def clear_all(self):
        if messagebox.askyesno("ยืนยัน", "คุณต้องการล้างข้อมูลทั้งหมดหรือไม่?"):
            self.students.clear()
            self.refresh_table()

    def export_csv(self):
        if not self.students:
            messagebox.showwarning("แจ้งเตือน", "ไม่มีข้อมูลสำหรับส่งออก")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            title="บันทึกไฟล์เกรดนักศึกษา"
        )

        if file_path:
            try:
                with open(file_path, mode="w", newline="", encoding="utf-8-sig") as file:
                    writer = csv.writer(file)
                    writer.writerow(["รหัสนักศึกษา", "ชื่อ-นามสกุล", "Midterm", "Final", "Total", "Grade"])
                    for s in self.students:
                        writer.writerow([s["id"], s["name"], s["midterm"], s["final"], s["total"], s["grade"]])
                messagebox.showinfo("สำเร็จ", f"บันทึกไฟล์เรียบร้อยแล้วที่:\n{file_path}")
            except Exception as e:
                messagebox.showerror("ข้อผิดพลาด", f"ไม่สามารถบันทึกไฟล์ได้: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GradingApp(root)
    root.mainloop()