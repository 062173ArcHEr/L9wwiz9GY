# 代码生成时间: 2025-09-23 20:01:51
import tkinter as tk
from tkinter import messagebox
import sqlite3

# Database configuration
DB_FILE = 'example.db'

"""
This function connects to the SQLite database.
"""
def connect_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except sqlite3.Error as e:
        messagebox.showerror('Database Connection Error', str(e))
        return None

"""
This function creates a table with proper constraints to prevent SQL injection.
"""
def create_table(conn):
    try:
        cursor = conn.cursor()
        # Using parameterized queries to prevent SQL injection
        cursor.execute("""CREATE TABLE IF NOT EXISTS users \
            (id INTEGER PRIMARY KEY, \
            username TEXT NOT NULL UNIQUE, \
            password TEXT NOT NULL)""")
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror('Create Table Error', str(e))

"""
This function inserts a user record into the database using parameterized queries.
"""
def insert_user(conn, username, password):
    try:
        cursor = conn.cursor()
        # Using parameterized queries to prevent SQL injection
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror('Insert User Error', str(e))

"""
This function fetches all user records from the database.
"""
def fetch_users(conn):
    try:
        cursor = conn.cursor()
        # Using parameterized queries to prevent SQL injection
        cursor.execute("SELECT * FROM users")
        return cursor.fetchall()
    except sqlite3.Error as e:
        messagebox.showerror('Fetch Users Error', str(e))
        return None

"""
This function initializes the GUI application.
"""
def init_gui():
    root = tk.Tk()
    root.title('SQL Injection Prevention Demo')
    
    # Layout configuration
    label_username = tk.Label(root, text='Username:')
    label_username.grid(row=0, column=0)
    entry_username = tk.Entry(root)
    entry_username.grid(row=0, column=1)
    
    label_password = tk.Label(root, text='Password:')
    label_password.grid(row=1, column=0)
    entry_password = tk.Entry(root, show='*')
    entry_password.grid(row=1, column=1)
    
    button_add = tk.Button(root, text='Add User', command=lambda: add_user(entry_username.get(), entry_password.get()))
    button_add.grid(row=2, column=0, columnspan=2)
    
    root.mainloop()

"""
This function handles the user addition process.
"""
def add_user(username, password):
    conn = connect_db()
    if conn is not None:
        create_table(conn)
        insert_user(conn, username, password)
        messagebox.showinfo('Success', 'User added successfully')

# Main execution
if __name__ == '__main__':
    init_gui()
