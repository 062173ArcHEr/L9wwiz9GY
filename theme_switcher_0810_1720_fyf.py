# 代码生成时间: 2025-08-10 17:20:10
import tkinter as tk
from tkinter import ttk

class ThemeSwitcher:
    """
    A class to handle theme switching in a Tkinter application.
    Allows switching between different themes for GUI elements.
    """
    def __init__(self, master):
        """
        Initialize the ThemeSwitcher with a Tkinter master window.
        :param master: The Tkinter master window object.
        """
        self.master = master
        self.master.title('Theme Switcher')
        self.master.geometry('300x200')

        # Define themes
        self.themes = {
            'Default': {
                'background': '#ffffff',
                'foreground': '#000000',
                'font': ('Helvetica', 10)
            },
            'Dark': {
                'background': '#333333',
                'foreground': '#dddddd',
                'font': ('Helvetica', 10, 'bold')
            }
        }

        # Current theme
        self.current_theme = 'Default'

        # Create a button to switch themes
        self.theme_switch_button = ttk.Button(self.master, text='Switch Theme', command=self.switch_theme)
        self.theme_switch_button.pack(pady=20)

    def switch_theme(self):
        """
        Switch the current theme to the next one.
        """
        # Get the list of theme names
        theme_names = list(self.themes.keys())

        # Find the index of the current theme and switch to the next one
        current_index = theme_names.index(self.current_theme)
        next_index = (current_index + 1) % len(theme_names)
        self.current_theme = theme_names[next_index]

        # Apply the new theme
        self.apply_theme(self.themes[self.current_theme])

    def apply_theme(self, theme):
        """
        Apply a given theme to the master window and its children.
        :param theme: A dictionary containing theme settings.
        """
        self.master.configure(bg=theme['background'])
        for widget in self.master.winfo_children():
            if isinstance(widget, ttk.Widget):
                widget.configure(style=f'TButton.{self.current_theme}')
                # Update all children to use the new colors and fonts
                widget.configure(bg=theme['background'], foreground=theme['foreground'], font=theme['font'])

        # Update the style for buttons
        style = ttk.Style()
        style.configure(f'TButton.{self.current_theme}', background=theme['background'], foreground=theme['foreground'], font=theme['font'])

if __name__ == '__main__':
    # Create the main window
    root = tk.Tk()

    # Create an instance of the ThemeSwitcher class
    theme_switcher = ThemeSwitcher(root)

    # Start the Tkinter event loop
    root.mainloop()