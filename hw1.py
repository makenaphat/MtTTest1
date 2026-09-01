
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------------------------------------------------------------
# Data: Content & Quiz for List and String (5 topics each)
# ---------------------------------------------------------------------------
DATA = {
    "List": [
        {
            "title": "1. การสร้าง List (Creation)",
            "theory": "List ใน Python เป็นโครงสร้างข้อมูลที่ใช้เก็บข้อมูลแบบเป็นลำดับ สามารถเก็บข้อมูลได้หลายประเภทพร้อมกัน\n\nตัวอย่าง:\nmy_list = [10, 20, 'Python', True]",
            "question": "ข้อใดคือการสร้าง List ที่ถูกต้องใน Python?",
            "options": ["a = (1, 2, 3)", "a = [1, 2, 3]", "a = {1, 2, 3}"],
            "answer": 1
        },
        {
            "title": "2. การเข้าถึงข้อมูลด้วย Index (Indexing)",
            "theory": "การอ้างอิงตำแหน่งใน List จะเริ่มนับจากตำแหน่งที่ 0 (Index 0)\nและสามารถใช้อินเด็กซ์ติดลบเพื่อดึงข้อมูลจากท้ายสุดได้ (-1 คือตัวสุดท้าย)\n\nตัวอย่าง:\nnums = [10, 20, 30]\nprint(nums[0]) # ได้ 10",
            "question": "ถ้า fruits = ['apple', 'banana', 'cherry'] แล้ว fruits[-1] มีค่าเป็นเท่าใด?",
            "options": ["'apple'", "'banana'", "'cherry'"],
            "answer": 2
        },
        {
            "title": "3. การเพิ่มข้อมูล (Adding Elements)",
            "theory": "ใช้วิธี append() เพื่อเพิ่มข้อมูลต่อท้าย List หรือ insert() เพื่อแทรกข้อมูลในตำแหน่งที่ต้องการ\n\nตัวอย่าง:\nitems = ['a']\nitems.append('b') # ['a', 'b']",
            "question": "คำสั่งใดใช้เพิ่มข้อมูลเข้าต่อท้าย List?",
            "options": ["append()", "add()", "push()"],
            "answer": 0
        },
        {
            "title": "4. การลบข้อมูล (Removing Elements)",
            "theory": "สามารถใช้ remove(val) ลบข้อมูลด้วยค่า, pop(index) ลบตามลำดับและคืนค่าออกมา, หรือ del ในการลบตัวแปร/ตำแหน่ง\n\nตัวอย่าง:\nnums = [1, 2, 3]\nnums.pop(0) # เหลือ [2, 3]",
            "question": "หากต้องการลบข้อมูลออกจาก List โดยระบุ 'ค่าของข้อมูล' ต้องใช้ฟังก์ชันใด?",
            "options": ["pop()", "remove()", "delete()"],
            "answer": 1
        },
        {
            "title": "5. การตัดแบ่งข้อมูล (Slicing)",
            "theory": "การดึงข้อมูลเฉพาะช่วง ใช้รูปแบบ list[start:stop]\nโดย stop คืออินเด็กซ์ที่จะไม่ถูกนับรวมเข้ามา\n\nตัวอย่าง:\nletters = ['a', 'b', 'c', 'd']\nprint(letters[0:2]) # ได้ ['a', 'b']",
            "question": "กำหนดให้ numbers = [0, 1, 2, 3, 4] ผลลัพธ์ของ numbers[1:3] คือข้อใด?",
            "options": ["[1, 2]", "[1, 2, 3]", "[0, 1, 2]"],
            "answer": 0
        }
    ],
    "String": [
        {
            "title": "1. พื้นฐาน String และ Immutability",
            "theory": "String คือข้อความที่ล้อมรอบด้วย ' ' หรือ \" \" โดยข้อมูลใน String ไม่สามารถแก้ไขค่าในตำแหน่งเดิมได้ (Immutable)\n\nตัวอย่าง:\ntext = 'Hello'",
            "question": "คุณสมบัติ Immutable ของ String หมายถึงข้อใด?",
            "options": [
                "ไม่สามารถเปลี่ยนตัวแปรได้",
                "ข้อมูลในตำแหน่งเดิมไม่สามารถแก้ไขตรงๆ ได้",
                "เก็บได้เฉพาะตัวอักษรภาษาอังกฤษ"
            ],
            "answer": 1
        },
        {
            "title": "2. การเชื่อมและการซ้ำ String (Concatenation & Repetition)",
            "theory": "ใช้เครื่องหมาย + ในการเชื่อม String เข้าด้วยกัน และใช้ * ในการทำซ้ำข้อความตามจำนวนรอบ\n\nตัวอย่าง:\n'Py' + 'thon' # ได้ 'Python'\n'Hi' * 2 # ได้ 'HiHi'",
            "question": "ผลลัพธ์ของคำสั่ง 'Go' * 3 คืออะไร?",
            "options": ["'Go 3'", "'GoGoGo'", "'Error'"],
            "answer": 1
        },
        {
            "title": "3. เมธอดเปลี่ยนตัวอักษร (upper, lower, strip)",
            "theory": ".upper() เปลี่ยนเป็นตัวพิมพ์ใหญ่ทั้งหมด\n.lower() เปลี่ยนเป็นตัวพิมพ์เล็กทั้งหมด\n.strip() ลบช่องว่างหัวและท้ายข้อความ\n\nตัวอย่าง:\n' hello '.strip() # ได้ 'hello'",
            "question": "เมธอดใดใช้ลบช่องว่างส่วนเกินที่หัวและท้ายข้อความ String?",
            "options": ["trim()", "clean()", "strip()"],
            "answer": 2
        },
        {
            "title": "4. การแยกและการรวม String (split & join)",
            "theory": ".split(sep) ใช้ตัดข้อความออกเป็น List ตามตัวแยกที่ระบุ\n.join(list) ใช้รวมสมาชิกใน List กลับมาเป็น String เดียวกัน\n\nตัวอย่าง:\n'a,b'.split(',') # ได้ ['a', 'b']",
            "question": "คำสั่ง 'a-b-c'.split('-') จะให้ผลลัพธ์แบบใด?",
            "options": ["['a', 'b', 'c']", "'abc'", "['a-b-c']"],
            "answer": 0
        },
        {
            "title": "5. การค้นหาและการแทนที่ (find & replace)",
            "theory": ".find(sub) ใช้หาตำแหน่งอินเด็กซ์แรกที่เจอข้อความ (หากไม่เจอได้ -1)\n.replace(old, new) ใช้แทนที่ข้อความเดิมด้วยข้อความใหม่\n\nตัวอย่าง:\n'cat'.replace('c', 'b') # ได้ 'bat'",
            "question": "หากใช้คำสั่ง 'Python'.find('z') ผลลัพธ์ที่ได้จะเป็นเท่าใด?",
            "options": ["0", "False", "-1"],
            "answer": 2
        }
    ]
}

# ---------------------------------------------------------------------------
# Application Class
# ---------------------------------------------------------------------------
class PythonLearningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("โปรแกรมสอนและทดสอบ Python: List & String")
        self.root.geometry("700x550")
        self.root.resizable(False, False)

        self.current_topic_type = "List"
        self.current_index = 0
        self.selected_option = tk.IntVar(value=-1)

        self.setup_ui()
        self.load_topic()

    def setup_ui(self):
        # Top Frame: Selector
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="เลือกหมวดหมู่เรียนรู้:", font=("Helvetica", 12, "bold")).pack(side=tk.LEFT, padx=5)
        
        self.topic_selector = ttk.Combobox(top_frame, values=["List", "String"], state="readonly", width=10, font=("Helvetica", 11))
        self.topic_selector.set("List")
        self.topic_selector.pack(side=tk.LEFT, padx=5)
        self.topic_selector.bind("<<ComboboxSelected>>", self.on_category_change)

        # Middle Frame: Theory & Code
        theory_frame = ttk.LabelFrame(self.root, text=" เนื้อหาการเรียนรู้ ", padding=10)
        theory_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.title_label = ttk.Label(theory_frame, text="", font=("Helvetica", 12, "bold"))
        self.title_label.pack(anchor=tk.W, pady=(0, 5))

        self.theory_text = tk.Text(theory_frame, height=7, wrap=tk.WORD, font=("Consolas", 10), bg="#f4f4f4")
        self.theory_text.pack(fill=tk.BOTH, expand=True)

        # Bottom Frame: Quiz
        quiz_frame = ttk.LabelFrame(self.root, text=" แบบทดสอบความเข้าใจ ", padding=10)
        quiz_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.question_label = ttk.Label(quiz_frame, text="", font=("Helvetica", 10, "bold"), wraplength=650)
        self.question_label.pack(anchor=tk.W, pady=(0, 5))

        self.radio_buttons = []
        for i in range(3):
            rb = ttk.Radiobutton(quiz_frame, text="", variable=self.selected_option, value=i)
            rb.pack(anchor=tk.W, pady=2)
            self.radio_buttons.append(rb)

        # Action & Navigation Frame
        nav_frame = ttk.Frame(self.root, padding=10)
        nav_frame.pack(fill=tk.X)

        self.check_btn = ttk.Button(nav_frame, text="ตรวจคำตอบ", command=self.check_answer)
        self.check_btn.pack(side=tk.LEFT, padx=5)

        self.prev_btn = ttk.Button(nav_frame, text="< หัวข้อก่อนหน้า", command=self.prev_topic)
        self.prev_btn.pack(side=tk.RIGHT, padx=5)

        self.next_btn = ttk.Button(nav_frame, text="หัวข้อถัดไป >", command=self.next_topic)
        self.next_btn.pack(side=tk.RIGHT, padx=5)

        self.page_label = ttk.Label(nav_frame, text="", font=("Helvetica", 10))
        self.page_label.pack(side=tk.RIGHT, padx=15)

    def load_topic(self):
        topic_data = DATA[self.current_topic_type][self.current_index]

        # Update Theory
        self.title_label.config(text=topic_data["title"])
        self.theory_text.config(state=tk.NORMAL)
        self.theory_text.delete("1.0", tk.END)
        self.theory_text.insert(tk.END, topic_data["theory"])
        self.theory_text.config(state=tk.DISABLED)

        # Update Quiz
        self.question_label.config(text=topic_data["question"])
        self.selected_option.set(-1)
        for i, option_text in enumerate(topic_data["options"]):
            self.radio_buttons[i].config(text=option_text)

        # Update Navigation state
        total_topics = len(DATA[self.current_topic_type])
        self.page_label.config(text=f"หัวข้อที่ {self.current_index + 1} / {total_topics}")
        self.prev_btn.config(state=tk.NORMAL if self.current_index > 0 else tk.DISABLED)
        self.next_btn.config(state=tk.NORMAL if self.current_index < total_topics - 1 else tk.DISABLED)

    def check_answer(self):
        selected = self.selected_option.get()
        if selected == -1:
            messagebox.showwarning("แจ้งเตือน", "กรุณาเลือกคำตอบก่อนส่ง!")
            return

        correct_acc = DATA[self.current_topic_type][self.current_index]["answer"]
        if selected == correct_acc:
            messagebox.showinfo("ผลการทดสอบ", "ถูกต้องครับ! เก่งมาก")
        else:
            messagebox.showerror("ผลการทดสอบ", "ยังไม่ถูกต้อง ลองทบทวนเนื้อหาแล้วตอบใหม่อีกครั้งนะ")

    def on_category_change(self, event):
        self.current_topic_type = self.topic_selector.get()
        self.current_index = 0
        self.load_topic()

    def next_topic(self):
        if self.current_index < len(DATA[self.current_topic_type]) - 1:
            self.current_index += 1
            self.load_topic()

    def prev_topic(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.load_topic()

if __name__ == "__main__":
    root = tk.Tk()
    app = PythonLearningApp(root)
    root.mainloop()

