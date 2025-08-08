# 代码生成时间: 2025-08-09 01:10:34
import tkinter as tk
ttk = tk.ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

"""
Interactive Chart Generator using Python and Tkinter.
This program allows users to input data and generate charts interactively.
"""

class InteractiveChartGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Interactive Chart Generator')
        self.geometry('600x400')
        self.create_widgets()

    def create_widgets(self):
        # Input frame
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        # Data entry widgets
        ttk.Label(self.input_frame, text='Data (comma-separated):').grid(row=0, column=0, padx=5)
        self.data_entry = ttk.Entry(self.input_frame, width=50)
        self.data_entry.grid(row=0, column=1, padx=5)

        # Chart type selection
        ttk.Label(self.input_frame, text='Chart Type:').grid(row=1, column=0, padx=5)
        self.chart_type = tk.StringVar()
        self.chart_type.set('line')  # default value
        ttk.OptionMenu(self.input_frame, self.chart_type, 'line', 'bar', 'pie').grid(row=1, column=1, padx=5)

        # Generate button
        ttk.Button(self, text='Generate Chart', command=self.generate_chart).pack(pady=20)

        # Canvas for displaying the plot
        self.figure = plt.Figure(figsize=(5, 3), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def generate_chart(self):
        try:
            # Get data from user input
            data_str = self.data_entry.get()
            data = [float(x) for x in data_str.split(',')]
            df = pd.DataFrame(data, columns=['Values'])

            # Create the chart based on the chart type
            if self.chart_type.get() == 'line':
                ax = self.figure.add_subplot(111)
                ax.plot(df['Values'])
            elif self.chart_type.get() == 'bar':
                ax = self.figure.add_subplot(111)
                ax.bar(df.index, df['Values'])
            elif self.chart_type.get() == 'pie':
                ax = self.figure.add_subplot(111)
                ax.pie(df['Values'], labels=df.index, autopct='%1.1f%%')

            # Redraw the canvas
            self.canvas.draw()
        except ValueError:
            # Handle non-numeric input
            tk.messagebox.showerror('Error', 'Please enter comma-separated numeric values.')
        except Exception as e:
            # Handle other exceptions
            tk.messagebox.showerror('Error', str(e))

    def run(self):
        self.mainloop()

if __name__ == '__main__':
    app = InteractiveChartGenerator()
    app.run()