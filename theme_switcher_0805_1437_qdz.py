# 代码生成时间: 2025-08-05 14:37:27
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor


class ThemeSwitcherApp:
    # Tuple of themes in the form of (background, foreground)
    THEMES = (
        ('light', ('#FFFFFF', '#000000')),
        ('dark', ('#333333', '#FFFFFF')),
        ('custom', ('#000000', '#FFFFFF'))
    )

    def __init__(self, root):
        self.root = root
        self.root.title("Theme Switcher")
        self.root.geometry("300x200")

        # Create a dictionary to store themes
        self.themes = {}
        for theme_name, (bg, fg) in self.THEMES:
            self.themes[theme_name] = {'bg': bg, 'fg': fg}

        # Set default theme to 'light'
        self.current_theme = 'light'
        self.apply_theme(self.current_theme)

        # Create theme selection menu
        theme_var = tk.StringVar()
        theme_var.set('light')  # default value
        self.theme_selector = ttk.OptionMenu(self.root, theme_var, *self.themes.keys(), command=self.change_theme)
        self.theme_selector.pack(pady=10)

        # Create a button to open color chooser for custom theme
        ttk.Button(self.root, text="Choose custom colors", command=self.choose_custom_colors).pack(pady=5)

    def apply_theme(self, theme_name):
        """Apply the selected theme to the GUI."""
        if theme_name in self.themes:
            theme = self.themes[theme_name]
            self.root.configure(bg=theme['bg'], fg=theme['fg'])
            self.current_theme = theme_name
        else:
            raise ValueError(f"Unknown theme: {theme_name}")

    def change_theme(self, theme_name):
        """Change the theme based on the user's selection."""
        try:
            self.apply_theme(theme_name)
        except ValueError as e:
            # Handle the error by printing to console
            print(e)

    def choose_custom_colors(self):
        """Allow user to choose custom colors and apply them as the theme."""
        bg_color = askcolor(title="Choose background color")[1]
        fg_color = askcolor(title="Choose foreground color")[1]
        if bg_color and fg_color:
            self.themes['custom'] = {'bg': bg_color, 'fg': fg_color}
            self.apply_theme('custom')

    def run(self):
        """Run the application."""
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ThemeSwitcherApp(root)
    app.run()
