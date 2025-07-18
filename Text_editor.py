import tkinter as tk
from tkinter import filedialog , messagebox

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path= filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files","*.txt")])
    if file_path:
        with open (file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert (tk.END , file.read())

def save_file():
    file_path= filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text file","*.txt")])
    if file_path:
        with open(file_path,'w')as file:
            file.write(text.get(1.0, tk.END))
            messagebox.showinfo("info","File saved successfully")

root=tk.Tk()
root.title("my notepad")
root.geometry("800x600")

menu=tk.Menu(root)
root.config(menu=menu)
file_menu=tk.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="open",command=open_file)
file_menu.add_command(label="save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=quit)

text=tk.Text(root, wrap=tk.WORD, font=("Helvetics",12),fg="black")
text.pack(expand=tk.YES,fill=tk.BOTH)

root.mainloop()