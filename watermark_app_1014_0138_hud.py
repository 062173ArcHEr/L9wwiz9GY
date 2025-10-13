# 代码生成时间: 2025-10-14 01:38:26
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
import io
import os

"""
数字水印技术实现
使用TKINTER框架创建图形界面，允许用户添加和提取水印。
"""

class WatermarkApp:
    def __init__(self, root):
        """初始化应用程序"""
        self.root = root
        self.root.title('数字水印技术')

        # 设置标签和按钮
        self.label = tk.Label(root, text='选择图片文件：')
        self.label.pack()

        self.open_button = tk.Button(root, text='打开', command=self.open_image)
        self.open_button.pack()

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.watermark_label = tk.Label(root, text='添加水印：')
        self.watermark_label.pack()

        self.watermark_entry = tk.Entry(root)
        self.watermark_entry.pack()

        self.add_button = tk.Button(root, text='添加水印', command=self.add_watermark)
        self.add_button.pack()

        self.remove_button = tk.Button(root, text='提取水印', command=self.remove_watermark)
        self.remove_button.pack()

    def open_image(self):
        """打开图片文件"""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.image_tk = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.image_tk)
            self.image_label.image = self.image_tk
        else:
            tk.messagebox.showerror('错误', '文件路径不能为空')

    def add_watermark(self):
        """添加水印"""
        try:
            watermark_text = self.watermark_entry.get()
            if not watermark_text:
                tk.messagebox.showerror('错误', '水印文本不能为空')
                return

            draw = ImageDraw.Draw(self.image)
            font = ImageFont.truetype('arial.ttf', 20)
            draw.text((10, 10), watermark_text, font=font, fill=(255, 255, 255))
            self.image.show()
        except Exception as e:
            tk.messagebox.showerror('错误', str(e))

    def remove_watermark(self):
        """提取水印"""
        try:
            # 这里需要实现提取水印的算法
            # 暂时用弹窗代替
            tk.messagebox.showinfo('提示', '提取水印功能暂未实现')
        except Exception as e:
            tk.messagebox.showerror('错误', str(e))

if __name__ == '__main__':
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()