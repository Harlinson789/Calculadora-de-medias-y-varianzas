import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate(lista):
    matrix = np.array(lista)
    
    calculations = {
        'mean': round(matrix.mean(), 2),
        'variance': round(matrix.var(), 2),
        'standard deviation': round(matrix.std(), 2),
        'max': round(matrix.max(), 2),
        'min': round(matrix.min(), 2),
        'sum': round(matrix.sum(), 2)
    }
    return calculations

class MeanVarStdApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mean, Variance, and Standard Deviation Calculator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")
        
        # Label and Entry for the list of numbers
        tk.Label(root, text="Ingrese los números separados por espacios:", bg="#f0f0f0", font=('Helvetica', 12)).pack(pady=10)
        self.entry = tk.Entry(root, font=('Helvetica', 12), width=50)
        self.entry.pack(pady=10)

        # Button
        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, bg="#4CAF50", fg="white", font=('Helvetica', 12), relief=tk.RAISED, borderwidth=2)
        self.calculate_button.pack(pady=10)

        # Textbox for displaying results
        self.result_text = tk.Text(root, height=15, width=70, font=('Helvetica', 12), wrap=tk.WORD, bg="#ffffff", padx=10, pady=10, borderwidth=2, relief=tk.SUNKEN)
        self.result_text.pack(pady=10)

    def calculate(self):
        try:
            numbers = list(map(float, self.entry.get().split()))
            results = calculate(numbers)
            self.result_text.delete(1.0, tk.END)
            result_text = ""
            for key, value in results.items():
                result_text += f"{key.capitalize()}: {value}\n"
            self.result_text.insert(tk.END, result_text)
        except ValueError as e:
            messagebox.showerror("Error", "Por favor, ingrese una lista válida de números.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MeanVarStdApp(root)
    root.mainloop()

