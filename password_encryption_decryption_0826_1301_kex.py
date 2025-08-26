# 代码生成时间: 2025-08-26 13:01:36
import tkinter as tk
from tkinter import messagebox
import base64
from cryptography.fernet import Fernet

# 生成密钥并保存到文件
def generate_key():
    return Fernet.generate_key()

# 从文件读取密钥
def load_key():
    key_file = open('secret.key', 'rb')
    return key_file.read()

# 保存密钥到文件
def save_key(key):
    key_file = open('secret.key', 'wb')
    key_file.write(key)
    key_file.close()

# 加密函数
def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())

# 解密函数
def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    try:
        return f.decrypt(encrypted_message).decode()
    except Exception as e:
        messagebox.showerror("Error", "Incorrect key or corrupted data.")
        return None

# GUI界面类
class PasswordEncryptionDecryptionApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Password Encryption Decryption Tool')
        
        # 输入框
        self.entry_label = tk.Label(master, text="Enter your password: ")
        self.entry_label.grid(row=0, column=0)
        self.entry = tk.Entry(master)
        self.entry.grid(row=0, column=1)
        
        # 加密按钮
        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
        self.encrypt_button.grid(row=1, column=0)
        
        # 解密按钮
        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
        self.decrypt_button.grid(row=1, column=1)
        
        # 显示结果的标签
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2)
        
        # 生成并保存密钥
        self.key = generate_key()
        save_key(self.key)
        
    def encrypt(self):
        message = self.entry.get()
        encrypted_message = encrypt_message(message, self.key)
        self.result_label.config(text=f"Encrypted: {encrypted_message}")
        
    def decrypt(self):
        message = self.entry.get()
        decrypted_message = decrypt_message(message, self.key)
        if decrypted_message:
            self.result_label.config(text=f"Decrypted: {decrypted_message}")
        else:
            self.result_label.config(text="")

# 主程序
if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordEncryptionDecryptionApp(root)
    root.mainloop()