from tkinter.filedialog import *
import tkinter as tk

from textblob import Word

def saveFile():
    new_file=asksaveasfile(mode='w', filetypes=[('text files', '.txt')])
    if new_file is None:
        return
    text=str(entry.get(1.0, tk.END))
    new_file.write(text)
    new_file.close()
    
def openFile():
    file=askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        content=file.read()
    entry.insert(tk.INSERT, content)

def clearFile():
    entry.delete(1.0, tk.END)

canvas= tk.Tk()
canvas.geometry("400x600")
canvas.title("Notepad")
canvas.config(bg="white")
top=tk.Frame(canvas)
top.pack(padx=10,pady=5, anchor='nw')

b1=tk.Button(canvas, text="Open", bg="#D4F0F0", command=openFile)
b1.pack(in_=top, side=tk.LEFT)

b2=tk.Button(canvas, text="Save", bg="#FFCCB6", command=saveFile)
b2.pack(in_=top, side=tk.LEFT)

b3=tk.Button(canvas, text="Clear", bg="#F3B0C3", command=clearFile)
b3.pack(in_=top, side=tk.LEFT)

b4=tk.Button(canvas, text="Exit", bg="#e2bef1", command=exit)
b4.pack(in_=top, side=tk.LEFT)

entry=tk.Text(canvas, wrap=tk.WORD, bg="#F2D4CC", font=("poppins",15))
entry.pack(padx=10,pady=5, expand=tk.TRUE, fill=tk.BOTH)

canvas.mainloop()
