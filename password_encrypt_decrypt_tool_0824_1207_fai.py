# 代码生成时间: 2025-08-24 12:07:08
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet


class PasswordEncryptDecryptTool:
    """
    密码加密解密工具类
    """
    def __init__(self, master):
        self.master = master
        self.master.title('Password Encrypt Decrypt Tool')
        self.fernet_key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.fernet_key)

        # 输入框
        self.input_label = tk.Label(master, text='Enter Password:')
        self.input_label.pack()
        self.input_entry = tk.Entry(master)
        self.input_entry.pack()

        # 按钮
        self.encrypt_button = tk.Button(master, text='Encrypt', command=self.encrypt)
        self.encrypt_button.pack()
        self.decrypt_button = tk.Button(master, text='Decrypt', command=self.decrypt)
        self.decrypt_button.pack()

        # 输出框
        self.output_label = tk.Label(master, text='')
        self.output_label.pack()

    def encrypt(self):
        """
        加密密码
        """
        try:
            password = self.input_entry.get()
            encrypted_password = self.cipher_suite.encrypt(password.encode())
            self.output_label.config(text=f'Encrypted: {encrypted_password}')
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def decrypt(self):
        """
        解密密码
        """
        try:
            password = self.input_entry.get()
            decrypted_password = self.cipher_suite.decrypt(password.encode())
            self.output_label.config(text=f'Decrypted: {decrypted_password}')
        except Exception as e:
            messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordEncryptDecryptTool(root)
    root.mainloop()