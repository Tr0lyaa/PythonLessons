import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    insert_values(num1 + num2)

def sub():
    num1, num2 = get_values()
    insert_values(num1 - num2)

def mul():
    num1, num2 = get_values()
    insert_values(num1 * num2)

def div():
    num1, num2 = get_values()
    if num2 != 0:
        insert_values(num1 / num2)
    else:
        insert_values('Деление на ноль!')

window = tk.Tk()
window.title('Калькулятор')
window.geometry('350x350')
window.resizable(False, False)

button_add = tk.Button(window, text='+', width = 2, height = 2, command = add)
button_add.grid(row=3, column=1, ipadx=20, ipady=6, padx=5, pady=5)
button_sub = tk.Button(window, text='-', width = 2, height = 2, command = sub)
button_sub.grid(row=3, column=2, ipadx=20, ipady=6, padx=5, pady=5)
button_mul = tk.Button(window, text='*', width = 2, height = 2, command = mul)
button_mul.grid(row=3, column=3, ipadx=20, ipady=6, padx=5, pady=5)
button_div = tk.Button(window, text='/', width = 2, height = 2, command = div)
button_div.grid(row=3, column=4, ipadx=20, ipady=6, padx=5, pady=5)

number1_entry = tk.Entry(window, width = 28)
number1_entry.grid(row=1, column=2, columnspan=3)
number2_entry = tk.Entry(window, width = 28)
number2_entry.grid(row=2, column=2, columnspan=3)
answer_entry = tk.Entry(window, width = 28)
answer_entry.grid(row=4, column=2, columnspan=3)

number1 = tk.Label(window, text = 'Введите первое число:')
number1.grid(row=1, column=1)
number2 = tk.Label(window, text = 'Введите второе число:')
number2.grid(row=2, column=1)
answer = tk.Label(window, text = 'Ответ:')
answer.grid(row=4, column=1)

window.mainloop()
