# 代码生成时间: 2025-08-04 17:48:19
import tkinter as tk
from tkinter import messagebox
import json

"""
API响应格式化工具GUI程序
"""

class ApiResponseFormatter:
    """API响应格式化工具类"""

    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title("API响应格式化工具")

        # 输入框
        self.input_label = tk.Label(master, text="输入API响应内容：")
        self.input_label.pack()
        self.input_text = tk.Text(master, height=10, width=50)
        self.input_text.pack()

        # 格式化按钮
        self.format_button = tk.Button(master, text="格式化", command=self.format_response)
        self.format_button.pack()

        # 输出框
        self.output_label = tk.Label(master, text="格式化后的API响应：")
        self.output_label.pack()
        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

    def format_response(self):
        """格式化API响应内容"""
        try:
            # 读取输入框内容
            response_content = self.input_text.get("1.0", "end-1c")
            # 尝试将内容解析为JSON
            response_json = json.loads(response_content)
            # 格式化JSON内容
            formatted_response = json.dumps(response_json, indent=4, ensure_ascii=False)
            # 将格式化后的内容显示在输出框
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", formatted_response)
        except json.JSONDecodeError as e:
            # 显示错误信息
            messagebox.showerror("JSON解析错误", str(e))

# 主程序
if __name__ == '__main__':
    # 创建主窗口
    root = tk.Tk()
    # 创建API响应格式化工具实例
    app = ApiResponseFormatter(root)
    # 运行主事件循环
    root.mainloop()