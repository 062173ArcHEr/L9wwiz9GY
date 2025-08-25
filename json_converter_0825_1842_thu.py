# 代码生成时间: 2025-08-25 18:42:37
import json
timport tkinter as tk
from tkinter import messagebox

"""
JSON数据格式转换器
"""

class JsonConverter:
    def __init__(self, root):
        """初始化UI界面"""
        self.root = root
        self.root.title("JSON数据格式转换器")

        # 输入框
        self.input_label = tk.Label(root, text="输入JSON数据")
        self.input_label.pack()
        self.input_text = tk.Text(root, height=10, width=50)
        self.input_text.pack()

        # 输出框
        self.output_label = tk.Label(root, text="转换后的JSON数据")
        self.output_label.pack()
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()

        # 转换按钮
        self.convert_button = tk.Button(root, text="转换", command=self.convert)
        self.convert_button.pack()

    def convert(self):
        """转换JSON数据"""
        try:
            # 从输入框获取JSON数据
            json_data = self.input_text.get("1.0", tk.END)
            # 尝试解析JSON数据
            data = json.loads(json_data)
            # 转换为JSON字符串
            json_string = json.dumps(data, ensure_ascii=False, indent=4)
            # 将转换后的JSON数据显示在输出框
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, json_string)
        except json.JSONDecodeError as e:
            # 显示错误信息
            messagebox.showerror("错误", f"解析JSON数据失败: {str(e)}")

if __name__ == '__main__':
    root = tk.Tk()
    app = JsonConverter(root)
    root.mainloop()