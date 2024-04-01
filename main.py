import tkinter as tk

def on_button_click(event):
    button_text = event.widget.cget("text")
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

root = tk.Tk()
root.title("Calculatrice")

entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

row_index = 1
col_index = 0

for button in buttons:
    btn = tk.Button(root, text=button, padx=20, pady=20)
    btn.grid(row=row_index, column=col_index)
    btn.bind("<Button-1>", on_button_click)
    col_index += 1
    if col_index > 3:
        col_index = 0
        row_index += 1

root.mainloop()
