def calculate():
    print("--- Simple Python Calculator ---")
    print("Select operation: +, -, *, /")
    
    while True:
        operator = input("\nEnter operator (or 'q' to quit): ")
        
        if operator.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if operator in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if operator == '+':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif operator == '-':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif operator == '*':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif operator == '/':
                    if num2 == 0:
                        print("Error! Division by zero.")
                    else:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid operator! Please use +, -, *, or /.")

if __name__ == "__main__":
    calculate()

    import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    current_text = entry.get()
    if button_text == "=":
        try:
            # eval() evaluates the string as a mathematical expression
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Initialize the window
root = tk.Tk()
root.title("Modern Calculator")
root.geometry("300x400")

# Display Area
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Button labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons
row_val = 1
col_val = 0
for button in buttons:
    action = lambda x=button: on_click(x)
    tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights so buttons resize
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()

import tkinter as tk
from tkinter import messagebox

# --- Styling Constants ---
COLOR_BG = "#202020"          # Dark background
COLOR_DISPLAY = "#333333"     # Slightly lighter display
COLOR_TEXT = "#FFFFFF"        # White text
COLOR_BTN_NUM = "#3b3b3b"     # Grey for numbers
COLOR_BTN_OPS = "#b3b3b3"     # Light grey for operators
COLOR_BTN_EQ = "#ff9500"      # Orange for the Equals button

def on_click(button_text):
    current = entry.get()
    if button_text == "=":
        try:
            # We replace '×' and '÷' back to '*' and '/' for Python to calculate
            expression = current.replace('×', '*').replace('÷', '/')
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Format")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Window Setup
root = tk.Tk()
root.title("VS Code Calc")
root.geometry("320x450")
root.configure(bg=COLOR_BG)

# The Display
entry = tk.Entry(root, font=("Helvetica", 32), bg=COLOR_DISPLAY, fg=COLOR_TEXT, 
                 borderwidth=0, justify='right', insertbackground='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=30, sticky="nsew")

# Button Layout (Rows and Columns)
buttons = [
    ('C', 1, 0), ('÷', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('×', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
]

# Creating Buttons with Style
for (text, row, col) in buttons:
    # Determine color based on type of button
    if text == "=":
        btn_color = COLOR_BTN_EQ
    elif text in ['+', '-', '×', '÷', 'C']:
        btn_color = COLOR_BTN_OPS
    else:
        btn_color = COLOR_BTN_NUM

    # "0" button spans two columns
    width_val = 1 if text != '0' else 2
    column_span = 1 if text != '0' else 2

    btn = tk.Button(root, text=text, font=("Helvetica", 16, "bold"),
                    bg=btn_color, fg="white" if text != 'C' else "black",
                    borderwidth=0, command=lambda t=text: on_click(t))
    
    btn.grid(row=row, column=col, columnspan=column_span, 
             padx=2, pady=2, sticky="nsew")

# Make the grid stretchable
for i in range(4): root.grid_columnconfigure(i, weight=1)
for i in range(1, 6): root.grid_rowconfigure(i, weight=1)

root.mainloop()

