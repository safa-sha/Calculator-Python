import tkinter as tk

just_calculated = False 

def click(value):
    global just_calculated
    operators = "+-*/"

    if value == "=":
        try:
            expression = entry.get()
            result = eval(expression)
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            just_calculated = True
        except ZeroDivisionError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Cannot divide by zero")
            just_calculated = True
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Invalid input")
            just_calculated = True

    elif value == "C":
        entry.delete(0, tk.END)
        just_calculated = False

    else:
        if just_calculated:
            if value in operators:
                just_calculated = False
            else:
                entry.delete(0, tk.END)
                just_calculated = False

        if value in operators:
            if entry.get() == "" or entry.get()[-1] in operators:
                return

        entry.insert(tk.END, value)

def key_press(event):
    if event.char in "0123456789+-*/":
        click(event.char)
    elif event.keysym == "Return":
        click("=")
    elif event.keysym == "BackSpace":
        entry.delete(len(entry.get()) - 1)


root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "C","0","=","+"
]

row = 1
col = 0

for b in buttons:
    tk.Button(
        root,
        text=b,
        width=5,
        height=2,
        font=("Arial", 18),
        command=lambda x=b: click(x)
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

root.bind("<Key>", key_press)

root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()

