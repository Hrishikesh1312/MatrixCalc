import tkinter as tk
from tkmacosx import Button
import numpy as np
from tkinter import messagebox

root = tk.Tk()
root.title("MatrixCalc")
root.geometry('575x700')
root['bg'] = '#5D6D7E'
root.resizable(0, 0)
font = 'Avenir 14'


def enter(event):
    adjoint_button['state'] = tk.NORMAL
    inverse_button['state'] = tk.NORMAL
    determinant_button['state'] = tk.NORMAL


def clear_matrix():
    matrix11.delete(0, 'end')
    matrix11['state'] = tk.DISABLED
    matrix12.delete(0, 'end')
    matrix12['state'] = tk.DISABLED
    matrix13.delete(0, 'end')
    matrix13['state'] = tk.DISABLED

    matrix21.delete(0, 'end')
    matrix21['state'] = tk.DISABLED
    matrix22.delete(0, 'end')
    matrix22['state'] = tk.DISABLED
    matrix23.delete(0, 'end')
    matrix23['state'] = tk.DISABLED

    matrix31.delete(0, 'end')
    matrix31['state'] = tk.DISABLED
    matrix32.delete(0, 'end')
    matrix32['state'] = tk.DISABLED
    matrix33.delete(0, 'end')
    matrix33['state'] = tk.DISABLED


def clear(event):
    global result_frame
    global labeldet

    clear_matrix()
    adjoint_button['state'] = tk.DISABLED
    inverse_button['state'] = tk.DISABLED
    determinant_button['state'] = tk.DISABLED

    clear_label = tk.Label(root, width=25, height=15, bg='#5D6D7E')
    clear_label.grid(row=13, column=0, rowspan=3, columnspan=3)

    try:
        labeldet.destroy()
    except NameError:
        pass


def replace():
    global row1
    global row2
    global row3
    for n, i in enumerate(row1):
        if i == '':
            row1[n] = 0
    for n, i in enumerate(row2):
        if i == '':
            row2[n] = 0
    try:
        for n, i in enumerate(row3):
            if i == '':
                row3[n] = '0'
    except NameError:
        pass


def constructor():
    global matrix
    global row1
    global row2
    global row3
    if matrix33['state'] == tk.DISABLED:
        row1 = [matrix11.get(), matrix12.get()]
        row2 = [matrix21.get(), matrix22.get()]
        replace()
        matrow1 = [float(s) for s in row1]
        matrow2 = [float(s) for s in row2]

        matrix = np.array([matrow1, matrow2])

    else:
        row1 = [matrix11.get(), matrix12.get(), matrix13.get()]
        row2 = [matrix21.get(), matrix22.get(), matrix23.get()]
        row3 = [matrix31.get(), matrix32.get(), matrix33.get()]
        replace()
        matrow1 = [float(s) for s in row1]
        matrow2 = [float(s) for s in row2]
        matrow3 = [float(s) for s in row3]

        matrix = np.array([matrow1, matrow2, matrow3])


def order2():
    matrix11['state'] = tk.NORMAL
    matrix12['state'] = tk.NORMAL
    matrix21['state'] = tk.NORMAL
    matrix22['state'] = tk.NORMAL

    matrix13['state'] = tk.DISABLED
    matrix23['state'] = tk.DISABLED
    matrix31['state'] = tk.DISABLED
    matrix32['state'] = tk.DISABLED
    matrix33['state'] = tk.DISABLED


def order3():
    matrix11['state'] = tk.NORMAL
    matrix12['state'] = tk.NORMAL
    matrix13['state'] = tk.NORMAL
    matrix21['state'] = tk.NORMAL
    matrix22['state'] = tk.NORMAL
    matrix23['state'] = tk.NORMAL
    matrix31['state'] = tk.NORMAL
    matrix32['state'] = tk.NORMAL
    matrix33['state'] = tk.NORMAL


def adj():
    global adjoint
    global result_frame

    constructor()
    if np.linalg.det(matrix) != 0:
        adjoint = np.around(np.linalg.inv(matrix) * np.linalg.det(matrix), 3)
        adjoint += 0
    else:
        messagebox.showinfo('Singular Matrix', 'The given matrix is singular. Singular matrices cannot have adjoints.')

    result_frame = tk.Frame(root)
    result_frame.grid(row=12, column=0, rowspan=3, columnspan=3)

    if matrix33['state'] == tk.DISABLED and np.linalg.det(matrix) != 0:

        label1 = tk.Label(result_frame, text=str(adjoint[0, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label2 = tk.Label(result_frame, text=str(adjoint[0, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label3 = tk.Label(result_frame, text=str(adjoint[1, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label4 = tk.Label(result_frame, text=str(adjoint[1, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')

        label1.grid(row=12, column=0)
        label2.grid(row=12, column=1)
        label3.grid(row=13, column=0)
        label4.grid(row=13, column=1)

    elif matrix33['state'] == tk.NORMAL and np.linalg.det(matrix) != 0:
        label1 = tk.Label(result_frame, text=str(adjoint[0, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label2 = tk.Label(result_frame, text=str(adjoint[0, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label3 = tk.Label(result_frame, text=str(adjoint[0, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label4 = tk.Label(result_frame, text=str(adjoint[1, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label5 = tk.Label(result_frame, text=str(adjoint[1, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label6 = tk.Label(result_frame, text=str(adjoint[1, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label7 = tk.Label(result_frame, text=str(adjoint[2, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label8 = tk.Label(result_frame, text=str(adjoint[2, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label9 = tk.Label(result_frame, text=str(adjoint[2, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')

        label1.grid(row=11, column=0)
        label2.grid(row=11, column=1)
        label3.grid(row=11, column=2)
        label4.grid(row=12, column=0)
        label5.grid(row=12, column=1)
        label6.grid(row=12, column=2)
        label7.grid(row=13, column=0)
        label8.grid(row=13, column=1)
        label9.grid(row=13, column=2)


def inv():
    global inverse
    global result_frame

    constructor()
    if np.linalg.det(matrix) != 0:
        inverse = np.around(np.linalg.inv(matrix), 3)
        inverse += 0
    else:
        messagebox.showinfo('Singular Matrix', 'The given matrix is singular. Singular matrices are not invertible.')

    result_frame = tk.Frame(root)
    result_frame.grid(row=12, column=0, rowspan=3, columnspan=3)

    if matrix33['state'] == tk.DISABLED and np.linalg.det(matrix) != 0:
        label1 = tk.Label(result_frame, text=str(inverse[0, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label2 = tk.Label(result_frame, text=str(inverse[0, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label3 = tk.Label(result_frame, text=str(inverse[1, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label4 = tk.Label(result_frame, text=str(inverse[1, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')

        label1.grid(row=12, column=0)
        label2.grid(row=12, column=1)
        label3.grid(row=13, column=0)
        label4.grid(row=13, column=1)

    elif matrix33['state'] == tk.NORMAL and np.linalg.det(matrix) != 0:
        label1 = tk.Label(result_frame, text=str(inverse[0, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label2 = tk.Label(result_frame, text=str(inverse[0, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label3 = tk.Label(result_frame, text=str(inverse[0, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label4 = tk.Label(result_frame, text=str(inverse[1, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label5 = tk.Label(result_frame, text=str(inverse[1, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label6 = tk.Label(result_frame, text=str(inverse[1, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label7 = tk.Label(result_frame, text=str(inverse[2, 0]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label8 = tk.Label(result_frame, text=str(inverse[2, 1]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')
        label9 = tk.Label(result_frame, text=str(inverse[2, 2]), height=3, width=8, font=font, bg='#283747',
                          relief='raised', fg='white')

        label1.grid(row=11, column=0)
        label2.grid(row=11, column=1)
        label3.grid(row=11, column=2)
        label4.grid(row=12, column=0)
        label5.grid(row=12, column=1)
        label6.grid(row=12, column=2)
        label7.grid(row=13, column=0)
        label8.grid(row=13, column=1)
        label9.grid(row=13, column=2)


def det():
    global determinant
    global labeldet
    constructor()
    determinant = round(np.linalg.det(matrix), 3)
    labeldet = tk.Label(button_frame, text='Δ = {0}'.format(str(determinant)), width=10, bg='#283747', fg='white',
                        relief='raised')
    labeldet.grid(row=8, column=2)


dbcolor = '#5D6D7E'

main_frame = tk.Frame(root, bd=3, bg='#5D6D7E', highlightthickness=0, highlightbackground='#5D6D7E')
main_frame.grid(row=3, column=0)

button_frame = tk.Frame(root, bd=3, bg='#5D6D7E')
button_frame.grid(row=8, column=0, rowspan=2, columnspan=3)

title_frame = tk.Frame(root, bd=3, bg='#5D6D7E')
title_frame.grid(row=2, column=0)

bottomFrame = tk.Frame(root)
bottomFrame.grid(row=14, column=0, columnspan=3)

head_label = tk.Label(root, text='MatrixCalc', bg='#283747', fg='white', font='Avenir 35 bold', width=20, height=4)
head_label.grid(row=0, column=0)

blank_text = 'Choose the order first \n Press Enter once you have entered the matrix \n Press Esc to clear'
blank_label = tk.Label(root, text=blank_text, bg='#5D6D7E', fg='black', font='Tahoma 10 bold', width=40, height=3)
blank_label.grid(row=11, column=0)

empty_label = tk.Label(root, bg='#5D6D7E', fg='black', font='Tahoma 10 bold', width=40, height=2)
blank_label.grid(row=11, column=0)

order_label = tk.Label(title_frame, text="ORDER", width=11, bg='#5D6D7E', font='Avenir 14 bold', borderwidth=2)
order_label.grid(row=2, column=1)

labelx = tk.Label(button_frame, text='', bg='#5D6D7E', width=10)
labelx.grid(row=9, column=1)

clear_label = tk.Label(root, width=25, height=15, bg='#5D6D7E')
clear_label.grid(row=12, column=0, rowspan=3, columnspan=3)

order_button1 = Button(title_frame, text='2 x 2', bg='#5D6D7E', font='Avenir 14 bold', width=100, height=30,
                       command=order2)
order_button1.grid(row=2, column=0)

order_button2 = Button(title_frame, text='3 x 3', bg='#5D6D7E', font='Avenir 14 bold', width=100, height=30,
                       command=order3)
order_button2.grid(row=2, column=2)

matrix11 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix11.grid(row=4, column=0)
matrix12 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix12.grid(row=4, column=1)
matrix13 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix13.grid(row=4, column=2)

matrix21 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix21.grid(row=5, column=0)
matrix22 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix22.grid(row=5, column=1)
matrix23 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix23.grid(row=5, column=2)

matrix31 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix31.grid(row=6, column=0)
matrix32 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix32.grid(row=6, column=1)
matrix33 = tk.Entry(main_frame, width=11, bg='#AEB6BF', font=font, disabledbackground=dbcolor, borderwidth=0,
                    state=tk.DISABLED, justify='center')
matrix33.grid(row=6, column=2)

adjoint_button = Button(button_frame, text='ADJOINT', bg='#AEB6BF', width=100, height=30, state=tk.DISABLED,
                        command=adj)
adjoint_button.grid(row=10, column=0)
determinant_button = Button(button_frame, text='DETERMINANT', bg='#AEB6BF', width=100, height=30, state=tk.DISABLED,
                            command=det)
determinant_button.grid(row=8, column=0)

inverse_button = Button(button_frame, text='INVERSE', bg='#AEB6BF', width=100, height=30, state=tk.DISABLED,
                        command=inv)
inverse_button.grid(row=10, column=2)

root.bind('<Return>', enter)
root.bind('<Escape>', clear)

root.mainloop()
