import tkinter as tk

root = tk.Tk()

def button_clicked():
    print('Button clicked')

button1 = tk.Button(root,
                    text='1',
                    command=button_clicked)
button2 = tk.Button(root,
                    text='2',
                    command=button_clicked)
button3 = tk.Button(root,
                    text='3',
                    command=button_clicked)
button4 = tk.Button(root,
                    text='4',
                    command=button_clicked)
button5 = tk.Button(root,
                    text='5',
                    command=button_clicked)
button6 = tk.Button(root,
                    text='6',
                    command=button_clicked)
button7 = tk.Button(root,
                    text='7',
                    command=button_clicked)
button8 = tk.Button(root,
                    text='8',
                    command=button_clicked)
button9 = tk.Button(root,
                    text='9',
                    command=button_clicked)
button0 = tk.Button(root,
                    text='0',
                    command=button_clicked)
button_clear = tk.Button(root,
                    text='clear',
                    command=button_clicked)
button_add = tk.Button(root,
                    text='+',
                    command=button_clicked)
button_sub = tk.Button(root,
                    text='-',
                    command=button_clicked)
button_div = tk.Button(root,
                    text='/',
                    command=button_clicked)
button_mult = tk.Button(root,
                    text='*',
                    command=button_clicked)
button_equ = tk.Button(root,
                    text='=',
                    command=button_clicked)
button_bpoint = tk.Button(root,
                    text='.',
                    command=button_clicked)


button1.grid(column=0, row=0, padx=5, pady=5)
button2.grid(column=1, row=0, padx=5, pady=5)
button3.grid(column=2, row=0, padx=5, pady=5)
button4.grid(column=0, row=1, padx=5, pady=5)
button5.grid(column=1, row=1, padx=5, pady=5)
button6.grid(column=2, row=1, padx=5, pady=5)
button7.grid(column=0, row=2, padx=5, pady=5)
button8.grid(column=1, row=2, padx=5, pady=5)
button9.grid(column=2, row=2, padx=5, pady=5)
button0.grid(column=0, row=3, padx=5, pady=5)
button_clear.grid(column=1, row=3, padx=5, pady=5)
button_add.grid(column=2, row=3, padx=5, pady=5)
button_sub.grid(column=0, row=4, padx=5, pady=5)
button_div.grid(column=1, row=4, padx=5, pady=5)
button_mult.grid(column=2, row=4, padx=5, pady=5)
button_equ.grid(column=0, row=5, padx=5, pady=5)
button_bpoint.grid(column=1, row=5, padx=5, pady=5)

root.mainloop()