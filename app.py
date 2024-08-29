import tkinter as tk
from tkinter import messagebox
import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz de 3x3
    matrix = np.array(lista).reshape(3, 3)
    
    # Calcular los valores para filas (axis=0), columnas (axis=1), y matriz aplanada
    calculations = {
        'mean': [round(val, 2) for val in matrix.mean(axis=0).tolist()] +
                [round(val, 2) for val in matrix.mean(axis=1).tolist()] +
                [round(matrix.mean(), 2)],
        'variance': [round(val, 2) for val in matrix.var(axis=0).tolist()] +
                    [round(val, 2) for val in matrix.var(axis=1).tolist()] +
                    [round(matrix.var(), 2)],
        'standard deviation': [round(val, 2) for val in matrix.std(axis=0).tolist()] +
                              [round(val, 2) for val in matrix.std(axis=1).tolist()] +
                              [round(matrix.std(), 2)],
        'max': [round(val, 2) for val in matrix.max(axis=0).tolist()] +
               [round(val, 2) for val in matrix.max(axis=1).tolist()] +
               [round(matrix.max(), 2)],
        'min': [round(val, 2) for val in matrix.min(axis=0).tolist()] +
               [round(val, 2) for val in matrix.min(axis=1).tolist()] +
               [round(matrix.min(), 2)],
        'sum': [round(val, 2) for val in matrix.sum(axis=0).tolist()] +
               [round(val, 2) for val in matrix.sum(axis=1).tolist()] +
               [round(matrix.sum(), 2)]
    }

    return calculations

class MeanVarStdApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mean, Variance, and Standard Deviation Calculator")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f0f0")  # Fondo gris claro
        
        # Labels and Entries
        self.labels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.entries = []
        for i, label in enumerate(self.labels):
            tk.Label(root, text=f"Number {label}:", bg="#f0f0f0", font=('Helvetica', 12)).grid(row=i//3, column=i%3*2, padx=5, pady=5)
            entry = tk.Entry(root, font=('Helvetica', 12))
            entry.grid(row=i//3, column=i%3*2+1, padx=5, pady=5)
            self.entries.append(entry)

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate, bg="#4CAF50", fg="white", font=('Helvetica', 12), relief=tk.RAISED, borderwidth=2)
        self.calculate_button.grid(row=3, column=0, columnspan=3, pady=10)

        self.result_text = tk.Text(root, height=15, width=70, font=('Helvetica', 12), wrap=tk.WORD, bg="#ffffff", padx=10, pady=10, borderwidth=2, relief=tk.SUNKEN)
        self.result_text.grid(row=4, column=0, columnspan=3)

    def calculate(self):
        try:
            numbers = [float(entry.get()) for entry in self.entries]
            results = calculate(numbers)
            self.result_text.delete(1.0, tk.END)
            result_text = ""
            for key, value in results.items():
                result_text += f"{key.capitalize()}:\n"
                result_text += "  " + ", ".join(map(str, value[:3])) + "\n"
                result_text += "  " + ", ".join(map(str, value[3:6])) + "\n"
                result_text += "  " + str(value[6]) + "\n\n"
            self.result_text.insert(tk.END, result_text)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MeanVarStdApp(root)
    root.mainloop()
