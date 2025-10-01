# 代码生成时间: 2025-10-01 21:25:39
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

"""
数据加密传输工具
使用Python和Tkinter框架创建的GUI应用程序
"""

class DataEncryptionToolbox:
    def __init__(self, master):
        """初始化GUI界面"""
        self.master = master
        self.master.title('数据加密传输工具')

        # 设置加密密钥
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

        # 创建输入框和标签
        self.create_widgets()

    def create_widgets(self):
        # 输入框：原文
        self.label_original = tk.Label(self.master, text='原文:')
        self.label_original.grid(row=0, column=0, sticky=tk.W)
        self.entry_original = tk.Entry(self.master, width=50)
        self.entry_original.grid(row=0, column=1)

        # 输入框：密文
        self.label_encrypted = tk.Label(self.master, text='密文:')
        self.label_encrypted.grid(row=1, column=0, sticky=tk.W)
        self.entry_encrypted = tk.Entry(self.master, width=50)
        self.entry_encrypted.grid(row=1, column=1)

        # 按钮：加密
        self.button_encrypt = tk.Button(self.master, text='加密', command=self.encrypt)
        self.button_encrypt.grid(row=2, column=0, columnspan=2, pady=10)

        # 按钮：解密
        self.button_decrypt = tk.Button(self.master, text='解密', command=self.decrypt)
        self.button_decrypt.grid(row=3, column=0, columnspan=2)

    def encrypt(self):
        """加密原文"""
        original_text = self.entry_original.get()
        if not original_text:
            messagebox.showwarning('警告', '原文不能为空！')
            return

        try:
            encrypted_text = self.cipher_suite.encrypt(original_text.encode())
            self.entry_encrypted.delete(0, tk.END)
            self.entry_encrypted.insert(0, encrypted_text.decode())
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def decrypt(self):
        """解密密文"""
        encrypted_text = self.entry_encrypted.get()
        if not encrypted_text:
            messagebox.showwarning('警告', '密文不能为空！')
            return

        try:
            decrypted_text = self.cipher_suite.decrypt(encrypted_text.encode())
            self.entry_original.delete(0, tk.END)
            self.entry_original.insert(0, decrypted_text.decode())
        except Exception as e:
            messagebox.showerror('错误', str(e))

def main():
    # 创建主窗口
    root = tk.Tk()
    # 创建DataEncryptionToolbox实例
    app = DataEncryptionToolbox(root)
    # 运行主循环
    root.mainloop()

if __name__ == '__main__':
    main()