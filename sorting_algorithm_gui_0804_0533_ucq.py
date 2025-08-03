# 代码生成时间: 2025-08-04 05:33:41
import tkinter as tk
a
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # 遍历所有数组元素
        for j in range(0, n-i-1):  # 最后i个元素已经是排好序的了
            if arr[j] > arr[j+1]:  # 交换如果发现元素e[j]比e[j+1]大，则交换之
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def sort_algorithm(event):
    try:
        arr = list(map(int, entry.get().split(',')))
        sorted_arr = eval(sort_method.get())(arr)
        label_result.config(text=f"Sorted Array: {sorted_arr}")
    except Exception as e:
        label_result.config(text=f"Error: {str(e)}")

def create_gui():
    root = tk.Tk()
    root.title("Sorting Algorithm GUI")

    # Create frame
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    # Create label and entry for array input
    label_array = tk.Label(frame, text="Enter array elements separated by comma: ")
    label_array.grid(row=0, column=0, padx=5, pady=5)
    entry = tk.Entry(frame)
    entry.grid(row=0, column=1, padx=5, pady=5)

    # Create label and combobox for sort method selection
    label_method = tk.Label(frame, text="Select sort method: ")
    label_method.grid(row=1, column=0, padx=5, pady=5)
    sort_methods = ["bubble_sort", "insertion_sort", "selection_sort"]
    sort_method = tk.StringVar(value=sort_methods[0])
    combobox = tk.OptionMenu(frame, sort_method, *sort_methods)
    combobox.grid(row=1, column=1, padx=5, pady=5)

    # Create button for sorting
    button_sort = tk.Button(frame, text="Sort", command=sort_algorithm)
    button_sort.grid(row=2, column=0, columnspan=2, pady=10)

    # Create label for result
    label_result = tk.Label(frame, text="")
    label_result.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    root.mainloop()

def main():
    create_gui()

def __name__ == "__main__":
    main()
