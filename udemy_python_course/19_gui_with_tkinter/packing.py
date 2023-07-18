import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

#tk.Label(root, text='Label 1', bg='green').pack(side='left') # glued to left side
#tk.Label(root, text='Label 2', bg='red').pack(side='top')  # glued to top

#tk.Label(root, text='Label 1', bg='green').pack(side='left', fill='y') # filled vertically
#tk.Label(root, text='Label 2', bg='red').pack(side='top', fill='x') # filled horizontally

#tk.Label(root, text='Label 1', bg='green').pack(side='left', fill='both') # filled as much space as possible
#tk.Label(root, text='Label 2', bg='red').pack(side='top', fill='both') # filled as much space as possible

tk.Label(main, text='Label 1', bg='green').pack(side='top', fill='both', expand=True)  # filled as much space as possible
tk.Label(main, text='Label 2', bg='red').pack(side='top', fill='both', expand=True)  # filled as much space as possible

tk.Label(root, text='Label Left', bg='blue').pack(side='left', fill='both', expand=True)

root.mainloop()