import tkinter as tk

m=tk.Tk()
count=0
label1Text=tk.StringVar()
label1Text.set(str(count))

def counting():
  global count
  count+=1
  label1Text.set(str(count))



m.title("Main Window")
button = tk.Button(m, text="Stop", width=25, command=lambda: m.destroy())
button.pack()

button2 = tk.Button(m, text="Counting", width=25, command=lambda: counting())
button2.pack()

label1 = tk.Label(m, borderwidth=2, relief="ridge", textvariable=label1Text, width=30)
label1.pack()
m.mainloop()