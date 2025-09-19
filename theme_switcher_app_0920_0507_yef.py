# 代码生成时间: 2025-09-20 05:07:58
import tkinter as tk
from tkinter import ttk

"""
A simple theme switcher application using Tkinter framework.
This application demonstrates how to change themes in a Tkinter application.
"""

class ThemeSwitcherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Theme Switcher")
        self.root.geometry("300x200")

        # Define themes
        self.themes = {
            "Light": ("white", "black"),
            "Dark": ("black", "white"),
        }

        # Set the default theme
        self.current_theme = "Light"
        self.bg_color, self.fg_color = self.themes[self.current_theme]

        # Create the theme switcher button
        self.theme_button = ttk.Button(self.root, text="Switch Theme", command=self.switch_theme)
        self.theme_button.pack(pady=20)

    def switch_theme(self):
        """
        Toggle the theme between Light and Dark.
        """
        if self.current_theme == "Light":
            self.current_theme = "Dark"
        else:
            self.current_theme = "Light"

        # Update the theme
        self.bg_color, self.fg_color = self.themes[self.current_theme]
        self.root.configure(bg=self.bg_color)
        self.theme_button.configure(bg=self.bg_color, fg=self.fg_color)

def main():
    """
    Main function to start the application.
    """
    root = tk.Tk()
    app = ThemeSwitcherApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()