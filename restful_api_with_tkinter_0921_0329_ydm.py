# 代码生成时间: 2025-09-21 03:29:27
import tkinter as tk
from tkinter import messagebox
from flask import Flask, request, jsonify
import threading

"""
This is a simple RESTful API server created using Flask and Tkinter.
It demonstrates how to create a basic API with Tkinter for a GUI interface.
"""

app = Flask(__name__)

# API endpoint to get a message
@app.route('/message', methods=['GET'])
def get_message():
    try:
        # Simulating some data retrieval
        message = {"message": "Hello, World!"}
        return jsonify(message)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to post a message
@app.route('/message', methods=['POST'])
def post_message():
    try:
        data = request.get_json()
        if 'message' not in data:
            raise ValueError("Missing 'message' in request data")

        # Simulating some data processing
        processed_message = data['message'].upper()
        return jsonify({'message': processed_message})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Function to run the Flask server in a separate thread
def run_server():
    threading.Thread(target=lambda: app.run(debug=False, use_reloader=False), daemon=True).start()

# Tkinter GUI setup
class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("RESTful API with Tkinter")
        self.create_widgets()

    def create_widgets(self):
        # Label
        self.label = tk.Label(self.root, text="RESTful API Server is running...")
        self.label.pack(pady=10)

        # Close button
        self.close_button = tk.Button(self.root, text="Close Server", command=self.stop_server)
        self.close_button.pack(pady=5)

    def start_server(self):
        run_server()
        messagebox.showinfo("Server Started", "The RESTful API server has started successfully.")

    def stop_server(self):
        # In a real-world scenario, you would implement a way to gracefully shutdown the server
        messagebox.showinfo("Server Stopped", "The RESTful API server has been stopped.")

# Main function to run the Tkinter application
def main():
    root = tk.Tk()
    app_gui = AppGUI(root)
    app_gui.start_server()
    root.mainloop()

if __name__ == '__main__':
    main()