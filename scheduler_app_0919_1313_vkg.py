# 代码生成时间: 2025-09-19 13:13:59
import tkinter as tk
from tkinter import ttk
import threading
from datetime import datetime, timedelta
import schedule
import time
"""
定时任务调度器应用
使用Python和Tkinter框架实现
"""
class SchedulerApp:
    def __init__(self, root):
        """初始化界面"""
        self.root = root
        self.root.title('定时任务调度器')
        self.root.geometry('300x200')
        self.tasks = []

        # 添加任务列表
        self.task_list = tk.Listbox(root)
        self.task_list.pack(padx=10, pady=10)

        # 添加任务按钮
        self.add_task_button = tk.Button(root, text='添加任务', command=self.add_task)
        self.add_task_button.pack(pady=5)

        # 开始调度按钮
        self.start_button = tk.Button(root, text='开始调度', command=self.start_scheduler)
        self.start_button.pack(pady=5)

        # 停止调度按钮
        self.stop_button = tk.Button(root, text='停止调度', command=self.stop_scheduler)
        self.stop_button.pack(pady=5)

    def add_task(self):
        """添加任务到列表"""
        task_name = simpledialog.askstring('输入', '请输入任务名称')
        if task_name:
            self.tasks.append(task_name)
            self.task_list.insert(tk.END, task_name)

    def start_scheduler(self):
        """开始调度任务"""
        self.scheduler_thread = threading.Thread(target=self.run_scheduler)
        self.scheduler_thread.start()

    def stop_scheduler(self):
        """停止调度任务"""
        self.scheduler_stop = True
        self.scheduler_thread.join()

    def run_scheduler(self):
        """运行调度任务"""
        self.scheduler_stop = False
        while not self.scheduler_stop:
            schedule.run_pending()
            time.sleep(1)

    def schedule_task(self, task_name, interval):
        """调度任务
        Args:
            task_name (str): 任务名称
            interval (int): 间隔时间（秒）
        """
        schedule.every(interval).seconds.do(self.execute_task, task_name)

    def execute_task(self, task_name):
        """执行任务
        Args:
            task_name (str): 任务名称
        """
        print(f'执行任务：{task_name} - {datetime.now()}')

if __name__ == '__main__':
    root = tk.Tk()
    app = SchedulerApp(root)
    root.mainloop()