# 代码生成时间: 2025-09-05 18:55:35
import tkinter as tk
from tkinter import messagebox
import json

# 定义一个函数，用于转换JSON数据格式
def convert_json_data(data):
    try:
        # 尝试将输入数据转换为JSON格式
        json_data = json.loads(data)
        # 将JSON数据转换为字符串格式
        return json.dumps(json_data, indent=4)
    except json.JSONDecodeError:
        # 如果输入数据不是有效的JSON格式，返回错误提示
        return "Invalid JSON data"

# 创建主窗口
def create_main_window():
    window = tk.Tk()
    window.title("JSON Data Formatter")
    
    # 创建输入文本框
    input_text = tk.Text(window, height=10, width=50)
    input_text.pack(pady=10)
    
    # 创建输出文本框
    output_text = tk.Text(window, height=10, width=50)
    output_text.pack(pady=10)
    
    # 创建转换按钮
    def on_convert_button_click():
        # 获取输入文本框的内容
        input_data = input_text.get("1.0", tk.END)
        # 调用转换函数
        formatted_data = convert_json_data(input_data)
        # 将转换后的数据设置到输出文本框
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", formatted_data)
        
    convert_button = tk.Button(window, text="Convert", command=on_convert_button_click)
    convert_button.pack(pady=10)
    
    return window

if __name__ == "__main__":
    # 创建并运行主窗口
    main_window = create_main_window()
    main_window.mainloop()