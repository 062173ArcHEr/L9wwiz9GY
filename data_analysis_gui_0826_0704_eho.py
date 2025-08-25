# 代码生成时间: 2025-08-26 07:04:03
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np

# 数据分析器GUI应用类
class DataAnalysisGUI:
    def __init__(self, root):
        """初始化GUI应用"""
        self.root = root
        root.title("数据分析师")
        
        # 创建文件选择按钮
        self.choose_button = tk.Button(root, text="选择文件", command=self.load_data)
        self.choose_button.pack()
        
        # 创建结果显示区域
        self.result_text = tk.Text(root, height=20, width=50)
        self.result_text.pack()
        
    def load_data(self):
        """加载数据文件"""
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                # 读取数据文件
                data = pd.read_csv(file_path)
                # 显示数据描述
                description = data.describe()
                # 将描述信息输出到文本框
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, str(description))
            except Exception as e:
                messagebox.showerror("错误", f"无法加载文件: {str(e)}")
        else:
            messagebox.showinfo("提示", "没有选择文件")

# 主函数
if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    
    # 实例化并运行应用
    app = DataAnalysisGUI(root)
    root.mainloop()