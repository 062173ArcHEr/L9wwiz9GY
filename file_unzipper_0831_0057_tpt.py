# 代码生成时间: 2025-08-31 00:57:15
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import zipfile
import os

"""
压缩文件解压工具，使用Python和Tkinter框架创建。
功能描述：允许用户选择压缩文件并解压到指定目录。
"""

class FileUnzipper:
    def __init__(self, master):
        # 初始化主窗口
        self.master = master
        master.title('文件解压工具')
# NOTE: 重要实现细节

        # 创建文件选择按钮
        self.btn_select = tk.Button(master, text='选择压缩文件', command=self.select_file)
        self.btn_select.pack()
# 改进用户体验

        # 创建解压按钮
        self.btn_unzip = tk.Button(master, text='解压文件', command=self.unzip_file, state='disabled')
        self.btn_unzip.pack()

        # 创建输出文本框显示解压信息
        self.txt_output = tk.Text(master, height=10, width=50)
        self.txt_output.pack()

        # 设置解压文件变量
        self.selected_file = None

    def select_file(self):
        # 选择文件
        self.selected_file = filedialog.askopenfilename(title='选择文件', filetypes=[('压缩文件', '*.zip *.rar')])
        if self.selected_file:
            # 启用解压按钮
            self.btn_unzip.config(state='normal')
            # 显示文件路径
            self.txt_output.delete(1.0, tk.END)
            self.txt_output.insert(tk.END, f'已选择文件：{self.selected_file}
')
        else:
            self.txt_output.insert(tk.END, '未选择文件
# 改进用户体验
')

    def unzip_file(self):
        # 解压文件
        if not self.selected_file:
            messagebox.showerror('错误', '请先选择文件')
            return

        self.txt_output.insert(tk.END, '开始解压...
')
        try:
            # 检查是否为zip文件
            if self.selected_file.endswith('.zip'):
                with zipfile.ZipFile(self.selected_file, 'r') as zip_ref:
                    zip_ref.extractall(os.path.dirname(self.selected_file))
                    self.txt_output.insert(tk.END, '解压完成
')
            else:
                self.txt_output.insert(tk.END, '不支持的文件类型
# NOTE: 重要实现细节
')
# 改进用户体验
        except zipfile.BadZipFile:
            self.txt_output.insert(tk.END, '文件损坏
')
        except Exception as e:
            self.txt_output.insert(tk.END, f'发生错误：{e}
')

# 创建Tkinter主窗口
root = tk.Tk()
# 优化算法效率
app = FileUnzipper(root)
root.mainloop()