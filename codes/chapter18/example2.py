import tkinter as tk
m=tk.Tk()
m.title("Main Window")
button = tk.Button(m, text="Stop", width=25, command=lambda: m.destroy())
button.pack()
m.mainloop()