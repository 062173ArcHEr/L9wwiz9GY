# 代码生成时间: 2025-07-31 09:19:57
import tkinter as tk
from tkinter import messagebox
import threading
import time
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

"""
定时任务调度器
"""

class TaskScheduler:
    def __init__(self, task, trigger, executor=None):
        """
        初始化定时任务调度器
        :param task: 任务函数
        :param trigger: 触发器
        :param executor: 执行器，默认为线程池
        """
        self.task = task
        self.trigger = trigger
        self.executor = executor if executor else ThreadPoolExecutor(10)

    def run(self):
        """
        运行定时任务
        """
        scheduler = BackgroundScheduler(executors={self.executor})
        scheduler.add_job(self.task, self.trigger)
        scheduler.start()
        print("定时任务调度器启动...")
        try:
            while True:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            scheduler.shutdown()


"""
定时任务函数示例
"""
def my_task():
    """
    定时执行的任务
    """
    try:
        print("任务执行...")
    except Exception as e:
        print(f"任务执行出错: {e}")

"""
创建Tkinter界面
"""
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("定时任务调度器")
        self.geometry("400x300")
        self.center_window()

        # 任务触发器
        self.task_trigger = tk.StringVar()
        self.task_trigger.set("0 */1 * * *")  # 默认每分钟执行一次

        # 创建输入框
        self.task_trigger_label = tk.Label(self, text="任务触发器（Cron表达式）")
        self.task_trigger_label.pack(pady=10)
        self.task_trigger_entry = tk.Entry(self, textvariable=self.task_trigger)
        self.task_trigger_entry.pack(pady=10)

        # 创建启动按钮
        self.start_button = tk.Button(self, text="启动任务", command=self.start_task)
        self.start_button.pack(pady=10)

        # 创建停止按钮
        self.stop_button = tk.Button(self, text="停止任务", command=self.stop_task)
        self.stop_button.pack(pady=10)

    def center_window(self):
        """
        居中窗口
        "