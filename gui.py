import tkinter as tk
from tkinter import messagebox

def and_gate(a, b):
    return a & b

def or_gate(a, b):
    return a | b

def half_adder(a, b):
    return (a ^ b, a & b)

def full_adder(a, b, cin):
    sum_ = a ^ b ^ cin
    cout = (a & b) | (b & cin) | (a & cin)
    return (sum_, cout)

def simulate():
    circuit = selected_circuit.get()
    try:
        if circuit == "AND Gate":
            a, b = int(entry1.get()), int(entry2.get())
            result = and_gate(a, b)
            messagebox.showinfo("Result", f"A={a}, B={b} => Y={result}")

        elif circuit == "OR Gate":
            a, b = int(entry1.get()), int(entry2.get())
            result = or_gate(a, b)
            messagebox.showinfo("Result", f"A={a}, B={b} => Y={result}")

        elif circuit == "Half Adder":
            a, b = int(entry1.get()), int(entry2.get())
            s, c = half_adder(a, b)
            messagebox.showinfo("Result", f"A={a}, B={b} => Sum={s}, Carry={c}")

        elif circuit == "Full Adder":
            a, b, cin = int(entry1.get()), int(entry2.get()), int(entry3.get())
            s, c = full_adder(a, b, cin)
            messagebox.showinfo("Result", f"A={a}, B={b}, Cin={cin} => Sum={s}, Cout={c}")
    except:
        messagebox.showerror("Error", "Invalid Input! Use 0 or 1.")

root = tk.Tk()
root.title("Digital Logic Simulator")

selected_circuit = tk.StringVar(value="AND Gate")
options = ["AND Gate", "OR Gate", "Half Adder", "Full Adder"]
tk.OptionMenu(root, selected_circuit, *options).pack()

tk.Label(root, text="Input A:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Input B:").pack()
entry2 = tk.Entry(root)
entry2.pack()

tk.Label(root, text="Cin (for Full Adder only):").pack()
entry3 = tk.Entry(root)
entry3.pack()

tk.Button(root, text="Simulate", command=simulate).pack()

root.mainloop()
