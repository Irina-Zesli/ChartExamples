# Примеры построения графиков

import tkinter as tk

# функция закрытия программы
def do_close():
    window.destroy()

window = tk.Tk()
window.geometry('450x450')
window.title("Примеры построения графиков")

#Добавление кнопки закрытия программы
button_close = tk.Button(window, text = "Закрыть", font = ('Hevletica', 10, 'bold'), command = do_close)
button_close.place(x = 330, y = 400, width = 90, height = 30)

window.mainloop()

