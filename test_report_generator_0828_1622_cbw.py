# 代码生成时间: 2025-08-28 16:22:21
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import json

# 定义一个函数来生成测试报告
def generate_report():
    # 获取用户选择的测试结果文件
    file_path = filedialog.askopenfilename(
        title="选择测试结果文件",
        filetypes=[("JSON 文件", "*.json"), ("所有文件", "*.*")]
    )

    # 检查文件路径是否有效
    if not file_path:
        messagebox.showerror("错误", "未选择文件")
        return

    # 读取测试结果文件
    try:
        with open(file_path, 'r') as file:
            test_results = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        messagebox.showerror("错误", f"读取文件失败：{e}")
        return

    # 生成测试报告内容
    report_content = "测试报告

"
    for test_case, result in test_results.items():
        report_content += f"测试用例：{test_case}
结果：{result}

"

    # 保存测试报告
    report_file_path = filedialog.asksaveasfilename(
        title="保存测试报告",
        defaultextension=".txt",
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")]
    )

    # 检查文件路径是否有效
    if not report_file_path:
        messagebox.showerror("错误", "未选择保存路径")
        return

    try:
        with open(report_file_path, 'w') as file:
            file.write(report_content)
        messagebox.showinfo("成功", "测试报告生成成功")
    except Exception as e:
        messagebox.showerror("错误", f"保存文件失败：{e}")

# 创建主窗口
root = tk.Tk()
root.title("测试报告生成器")

# 创建按钮，点击后调用生成报告的函数
generate_button = tk.Button(root, text="生成测试报告", command=generate_report)
generate_button.pack(pady=20)

# 运行主循环
root.mainloop()