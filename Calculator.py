import tkinter as tk

root = tk.Tk()
root.title('Calculator')

calculation = ''

def button_clicked(number):
    print(f'Button {number} clicked')
    display.set(calculation)


display = tk.StringVar()
button1 = tk.Button(root,
                    text='1',
                    command=lambda: button_clicked('1'),
                    height=2,
                    width=5)
button2 = tk.Button(root,
                    text='2',
                    command=lambda: button_clicked('2'),
                    height=2,
                    width=5)
button3 = tk.Button(root,
                    text='3',
                    command=lambda: button_clicked('3'),
                    height=2,
                    width=5)
button4 = tk.Button(root,
                    text='4',
                    command=lambda: button_clicked('4'),
                    height=2,
                    width=5)
button5 = tk.Button(root,
                    text='5',
                    command=lambda: button_clicked('5'),
                    height=2,
                    width=5)
button6 = tk.Button(root,
                    text='6',
                    command=lambda: button_clicked('6'),
                    height=2,
                    width=5)
button7 = tk.Button(root,
                    text='7',
                    command=lambda: button_clicked('7'),
                    height=2,
                    width=5)
button8 = tk.Button(root,
                    text='8',
                    command=lambda: button_clicked('8'),
                    height=2,
                    width=5)
button9 = tk.Button(root,
                    text='9',
                    command=lambda: button_clicked('9'),
                    height=2,
                    width=5)
button0 = tk.Button(root,
                    text='0',
                    command=lambda: button_clicked('0'),
                    height=2,
                    width=5)
button_clear = tk.Button(root,
                    text='clear',
                    command=lambda: button_clicked('clear'),
                    height=2,
                    width=5)
button_add = tk.Button(root,
                    text='+',
                    command=lambda: button_clicked('+'),
                    height=2,
                    width=5)
button_sub = tk.Button(root,
                    text='-',
                    command=lambda: button_clicked('-'),
                    height=2,
                    width=5)
button_div = tk.Button(root,
                    text='/',
                    command=lambda: button_clicked('/'),
                    height=2,
                    width=5)
button_mult = tk.Button(root,
                    text='*',
                    command=lambda: button_clicked('*'),
                    height=2,
                    width=5)
button_equ = tk.Button(root,
                    text='=',
                    command=lambda: button_clicked('='),
                    height=2,
                    width=5)
button_bpoint = tk.Button(root,
                    text='.',
                    command=lambda: button_clicked('.'),
                    height=2,
                    width=5)


button1.grid(column=0, row=0, padx=5, pady=5)
button2.grid(column=1, row=0, padx=5, pady=5)
button3.grid(column=2, row=0, padx=5, pady=5)
button4.grid(column=0, row=1, padx=5, pady=5)
button5.grid(column=1, row=1, padx=5, pady=5)
button6.grid(column=2, row=1, padx=5, pady=5)
button7.grid(column=0, row=2, padx=5, pady=5)
button8.grid(column=1, row=2, padx=5, pady=5)
button9.grid(column=2, row=2, padx=5, pady=5)
button0.grid(column=1, row=3, padx=5, pady=5)
button_clear.grid(column=3, row=0, padx=5, pady=5)
button_add.grid(column=3, row=1, padx=5, pady=5)
button_sub.grid(column=3, row=2, padx=5, pady=5)
button_div.grid(column=2, row=3, padx=5, pady=5)
button_mult.grid(column=0, row=3, padx=5, pady=5)
button_equ.grid(column=3, row=3, padx=5, pady=5)
button_bpoint.grid(column=0, row=4, padx=5, pady=5)

root.mainloop()