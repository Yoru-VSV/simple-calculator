import tkinter as tk
from calclogic import optellen, aftrekken, vermenigvuldigen, delen

operations = {
    "+": optellen,
    "-": aftrekken,
    "*": vermenigvuldigen,
    "/": delen,
}

first_value = None
pending_op = None

def click(value):
    global first_value, pending_op

    if value == "C":
        first_value = None
        pending_op = None
        entry_var.set("")

    elif value in operations:
        if entry_var.get() == "":
            return
        first_value = float(entry_var.get())
        pending_op = value
        entry_var.set("")

    elif value == "=":
        if pending_op is None or entry_var.get() == "":
            return
        second_value = float(entry_var.get())
        result = operations[pending_op](first_value, second_value)
        entry_var.set(str(result))
        first_value = None
        pending_op = None

    else:
        entry_var.set(entry_var.get() + str(value))

root = tk.Tk()
root.title("Simple Calculator")
root.resizable(False, False)

entry_var = tk.StringVar()

display = tk.Entry(
    root, textvariable=entry_var, font=("Arial", 20),
    justify="right", bd=8, relief="ridge"
)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10, sticky="ew")

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
]

for (text, row, col) in buttons:
    tk.Button(
        root, text=text, font=("Arial", 16), width=4, height=2,
        command=lambda t=text: click(t)
    ).grid(row=row, column=col, padx=3, pady=3)

tk.Button(
    root, text="=", font=("Arial", 16), width=20, height=2,
    bg="#4caf50", fg="white", command=lambda: click("=")
).grid(row=5, column=0, columnspan=4, padx=3, pady=3, sticky="ew")

root.mainloop()