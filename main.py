import tkinter as tk
from tkinter import ttk
import sorting as s
import visualizer as vs
import numpy as np
import random

class SortingVisualizerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sorting Algorithm Visualizer")

        self.array_size = 100
        self.algorithm_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Algorithm selection
        algorithm_label = tk.Label(self.master, text="Select Sorting Algorithm:")
        algorithm_label.place(x=30,y=10)

        algorithm_combobox = ttk.Combobox(self.master, textvariable=self.algorithm_var,
                                          values=['bubble_sort', 'heap_sort', 'selection_sort', 'insertion_sort', 'quick_sort', 'merge_sort'])
        algorithm_combobox.place(x=30,y=30)

        # Start button
        start_button = tk.Button(self.master, text="Start Visualization", command=self.start_visualization, border= 3)
        start_button.place(x=45,y=60)

        l1 =tk.Label(self.master,text="A project made by \nAyush and Kaamil",border=1)
        l1.place(x=42,y=90)  

    def start_visualization(self):
        selected_algorithm = self.algorithm_var.get()
        if selected_algorithm:
            algorithm = getattr(s, selected_algorithm, None)

            if algorithm is None:
                tk.messagebox.showerror("Error", "Invalid algorithm selection.")
                return

            arr = s.Array(get_random_array(self.array_size))
            algorithm(arr)

            plotter = vs.Plotter(arr.pile, title=selected_algorithm, repeat=True, interval=2)
            plotter.plot()

def get_random_array(length):
    n = list(range(length))
    random.shuffle(n)
    return n

def main():
    root = tk.Tk()
    app = SortingVisualizerApp(root)
    root.geometry("200x130")
    root.mainloop()

if __name__ == "__main__":
    main()