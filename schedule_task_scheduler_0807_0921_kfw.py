# 代码生成时间: 2025-08-07 09:21:54
import tkinter as tk
from tkinter import messagebox
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
import logging

# 设置日志
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

class ScheduleTaskScheduler:
    """定时任务调度器"""

    def __init__(self, master: tk.Tk):
        "