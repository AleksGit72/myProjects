"""
создание графического интерфейса с
кнопкой, надписью и полем ввода
"""
from tkinter import *  # подключение модуля tkinter
root = Tk()  # создание главного окна
btn = Button(root, text='Кнопочка', width=10, height=2, bg='white', fg='black', font='Liberation 14')  # создание кнопки
lab = Label(root, text='Ваша фамилия:', font='Arial 14')  # создание надписи
Edit = Entry(root, width=20)  # создание поля ввода
btn . pack()  # размещение кнопки на форме
lab . pack()  # размещение надписи на форме
Edit . pack()  # размещение поля ввода на форме
root . mainloop()  # отображение главного окна
