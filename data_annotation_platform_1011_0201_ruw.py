# 代码生成时间: 2025-10-11 02:01:28
import tkinter as tk
from tkinter import filedialog, messagebox

"""
数据标注平台，使用Python和Tkinter框架创建。
该程序允许用户在图形界面中打开图片文件，并对图片进行标注。
"""

class DataAnnotationPlatform:
    """数据标注平台的主类"""
    def __init__(self, root):
        self.root = root
        self.root.title("数据标注平台")

        # 设置窗口大小
        self.root.geometry("800x600")

        # 创建菜单栏
        self.create_menu()

        # 创建图片显示框架
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(padx=10, pady=10)

        # 创建标注控件
        self.canvas = tk.Canvas(self.image_frame, width=400, height=400, bg="white")
        self.canvas.pack()

    def create_menu(self):
        """创建菜单栏"""
        menubar = tk.Menu(self.root)

        # 文件菜单
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="打开图片", command=self.open_image)
        file_menu.add_separator()
        file_menu.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="文件", menu=file_menu)

        self.root.config(menu=menubar)

    def open_image(self):
        """打开图片文件"""
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if not filepath:
            return

        try:
            self.load_image(filepath)
        except Exception as e:
            messagebox.showerror("错误", str(e))

    def load_image(self, filepath):
        """加载图片到画布"""
        self.image_path = filepath
        self.image = tk.PhotoImage(file=filepath)
        self.canvas.create_image(0, 0, image=self.image, anchor=tk.NW)

# 创建Tkinter窗口
root = tk.Tk()
app = DataAnnotationPlatform(root)

# 运行程序
root.mainloop()