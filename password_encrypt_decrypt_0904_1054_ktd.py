# 代码生成时间: 2025-09-04 10:54:01
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

"""
密码加密解密工具
"""

# 定义一个类，用于创建GUI界面和处理加密解密逻辑
class PasswordEncryptDecryptApp:
    def __init__(self, master):
        # 设置窗口标题
        master.title("Password Encrypt Decrypt Tool")

        # 创建输入框和滚动条
        self.input_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10)
        self.input_text.pack(expand=True, fill=tk.BOTH)

        # 创建按钮
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # 创建输出框和滚动条
        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=10)
        self.output_text.pack(expand=True, fill=tk.BOTH)

        # 初始化密钥
        self.key = get_random_bytes(16)

    def encrypt(self):
        # 获取输入框的内容
        input_text = self.input_text.get("1.0", tk.END)

        # 检查输入是否为空
        if not input_text.strip():
            messagebox.showerror("Error", "Input is empty")
            return

        try:
            # 加密输入内容
            ciphertext = self.encrypt_text(input_text)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", ciphertext)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt(self):
        # 获取输出框的内容
        output_text = self.output_text.get("1.0", tk.END)

        # 检查输入是否为空
        if not output_text.strip():
            messagebox.showerror("Error", "Output is empty")
            return

        try:
            # 解密输出内容
            plaintext = self.decrypt_text(output_text)
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert("1.0", plaintext)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def encrypt_text(self, plaintext):
        # 使用AES加密算法加密文本
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
        iv = b64encode(cipher.iv).decode("utf-8")
        ct = b64encode(ct_bytes).decode("utf-8")
        return f"{iv}:{ct}"

    def decrypt_text(self, encrypted_text):
        # 使用AES解密算法解密文本
        iv, ct = encrypted_text.split(":")
        iv = b64decode(iv)
        ct = b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        return pt.decode("utf-8")

# 创建主窗口
root = tk.Tk()

# 创建应用实例
app = PasswordEncryptDecryptApp(root)

# 运行主循环
root.mainloop()