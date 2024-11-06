import tkinter as tk
import ttkbootstrap as ttk

def convert():
    try:
        mile_input = float(entyINt.get())
        km_output = mile_input * 1.61
        output_str.set(f"{km_output:.2f} km")
    except ValueError:
        output_str.set("Invalid input")

# Window
window = ttk.Window(themename='darkly')
window.title('Converter')
window.geometry('300x150')

# Title
title_label = ttk.Label(master=window, text='Miles to Kilometers', font='Calibri 24 bold')
title_label.pack()

# Input field
input_frame = ttk.Frame(master=window)
entyINt = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entyINt)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# Output
output_str = tk.StringVar()
output_label = ttk.Label(master=window, font='Calibri 24', textvariable=output_str)
output_label.pack(pady=10)

window.mainloop()
