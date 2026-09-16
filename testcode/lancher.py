import os
import sys
import subprocess
import tkinter as tk
from tkinter import messagebox

# หา Directory ปัจจุบันที่ไฟล์ lancher.py อยู่
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# รายชื่อไฟล์ทั้ง 5 ไฟล์ที่ต้องการสร้างปุ่มเรียกใช้งาน
TARGET_FILES = [
    "casting.py",
    "mamyvaltomalvar.py",
    "onevaltomalvar.py",
    "Output Variables.py",
    "Single or Double.py"
]

def run_script(filename):
    """ฟังก์ชันสำหรับสั่งรันไฟล์ Python ที่เลือก"""
    file_path = os.path.join(BASE_DIR, filename)
    
    if os.path.exists(file_path):
        try:
            # ใช้ sys.executable เพื่ออ้างอิง Python Environment ตัวเดียวกับที่รัน Launcher อยู่
            subprocess.Popen([sys.executable, file_path])
        except Exception as e:
            messagebox.showerror("Error", f"ไม่สามารถรันไฟล์ได้: {e}")
    else:
        messagebox.showwarning("File Not Found", f"ไม่พบไฟล์: {filename}")

# --- สร้างหน้าต่างหลัก GUI ---
root = tk.Tk()
root.title("Python Script Launcher")
root.geometry("350x380")
root.configure(bg="#1e1e1e") # ปรับโทนสีเข้มเข้ากับ VS Code

# หัวข้อ GUI
label = tk.Label(
    root, 
    text="เลือกโปรแกรมที่ต้องการรัน", 
    font=("Tahoma", 12, "bold"), 
    fg="#ffffff", 
    bg="#1e1e1e",
    pady=15
)
label.pack()

# สร้างปุ่ม 5 ปุ่มวนลูปตามรายการ TARGET_FILES
for filename in TARGET_FILES:
    btn = tk.Button(
        root,
        text=f"▶ Run {filename}",
        font=("Tahoma", 10),
        bg="#007acc",
        fg="white",
        activebackground="#005999",
        activeforeground="white",
        relief="flat",
        cursor="hand2",
        width=28,
        pady=6,
        command=lambda f=filename: run_script(f)
    )
    btn.pack(pady=6)

# เริ่มทำงานหน้าต่าง GUI
root.mainloop()