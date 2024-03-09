import tkinter as tk
from tkinter import ttk

def convert():
    try:
        input_value = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Meters":
            if to_unit == "Feet":
                converted_value = input_value * 3.28084
            elif to_unit == "Yards":
                converted_value = input_value * 1.09361
            else:
                converted_value = input_value

        elif from_unit == "Feet":
            if to_unit == "Meters":
                converted_value = input_value / 3.28084
            elif to_unit == "Yards":
                converted_value = input_value / 3
            else:
                converted_value = input_value

        elif from_unit == "Yards":
            if to_unit == "Meters":
                converted_value = input_value / 1.09361
            elif to_unit == "Feet":
                converted_value = input_value * 3
            else:
                converted_value = input_value

        result_label.config(text=f"Result: {converted_value:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a number.")

root = tk.Tk()
root.geometry("600x600")
root.title("Unit Converter App")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=10, pady=10)

units = ["Metres", "Feet", "Yards"]

from_var = tk.StringVar(value=units[0])
to_var = tk.StringVar(value=units[1])

from_dropdown = tk.OptionMenu(root, from_var, *units)
to_dropdown = tk.OptionMenu(root, to_var, *units)

from_dropdown.grid(row=0, column=1, padx=10, pady=10)
to_dropdown.grid(row=0, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert)
convert_button.grid(row=1, column=9, columnspan=3, pady=10)

result_label = tk.Label(root, text="Result: ")
result_label.grid(row=1, column=0, columnspan=3)

root.mainloop()