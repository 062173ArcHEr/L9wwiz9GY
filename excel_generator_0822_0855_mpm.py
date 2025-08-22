# 代码生成时间: 2025-08-22 08:55:29
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import xlsxwriter

"""Excel表格自动生成器"""

class ExcelGenerator:
    """Excel表格自动生成器类"""
    def __init__(self, root):
        self.root = root
        self.file_path = ''
        self.setup_ui()

    def setup_ui(self):
        """设置UI界面"""
        self.root.title('Excel表格自动生成器')
        self.root.geometry('500x300')

        # 创建按钮，点击后选择文件生成Excel
        button_generate = tk.Button(self.root, text='生成Excel', command=self.generate_excel)
        button_generate.pack(pady=20)

        # 创建文本框显示文件路径
        self.text_file_path = tk.Text(self.root, height=1, width=50)
        self.text_file_path.pack(pady=20)

    def generate_excel(self):
        """生成Excel文件"""
        try:
            # 选择文件
            self.file_path = filedialog.askopenfilename()
            if not self.file_path:
                messagebox.showerror('错误', '未选择文件')
                return

            # 读取文件并生成Excel
            self.text_file_path.delete(1.0, tk.END)
            self.text_file_path.insert(tk.END, self.file_path)
            self.create_excel(self.file_path)
            messagebox.showinfo('成功', 'Excel文件生成成功')
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def create_excel(self, file_path):
        """根据文件生成Excel"""
        try:
            # 读取文件
            df = pd.read_csv(file_path)

            # 创建Excel文件
            output_file = 'output.xlsx'
            writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
            df.to_excel(writer, index=False, sheet_name='Sheet1')
            writer.save()
        except Exception as e:
            print(f'生成Excel文件失败: {str(e)}')

def main():
    """主函数"""
    root = tk.Tk()
    app = ExcelGenerator(root)
    root.mainloop()

if __name__ == '__main__':
    main()