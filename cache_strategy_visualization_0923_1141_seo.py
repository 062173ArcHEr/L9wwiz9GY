# 代码生成时间: 2025-09-23 11:41:20
import tkinter as tk
from tkinter import messagebox

class CacheStrategyVisualization:
    def __init__(self, master, cache_size):
        """Initialize the cache strategy visualization."""
        self.master = master
        self.cache_size = cache_size
        self.cache = {}
        self.cache_keys = []
        self.items = []
        self.create_widgets()

    def create_widgets(self):
        "