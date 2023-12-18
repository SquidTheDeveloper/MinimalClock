import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

def move_clock(event):
    x, y = 0, 0
    if event.keysym == 'Up':
        y -= 10
    elif event.keysym == 'Down':
        y += 10
    elif event.keysym == 'Left':
        x -= 10
    elif event.keysym == 'Right':
        x += 10
    root.geometry('+{}+{}'.format(root.winfo_x() + x, root.winfo_y() + y))

root = tk.Tk()

root.title("Digital Clock")
root.attributes('-transparentcolor', 'black')
root.wm_attributes('-topmost', True)
root.overrideredirect(True)

custom_font = ('Cascadia Code', 40, 'bold')

label = tk.Label(root, font=custom_font, bg='black', fg='white')
label.pack(anchor='center')

time()

root.bind_all('<Control-Up>', move_clock)
root.bind_all('<Control-Down>', move_clock)
root.bind_all('<Control-Left>', move_clock)
root.bind_all('<Control-Right>', move_clock)

root.mainloop()