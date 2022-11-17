# Примеры построения графиков

import tkinter as tk
import chart1
import chart2
import chart3
import chart4

# функция закрытия программы
def do_close():
    window.destroy()

window = tk.Tk()
window.geometry('450x550')
window.title("Примеры построения графиков")

#Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Hevletica', 16, 'bold'), fg = '#0000cc')
lblTitle.place(x = 55, y = 25)

#Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text = "График 1", font = ('Hevletica', 10, 'bold'), command = chart1.plot_chart)
btnChart1.place(x = 40, y = 115, width = 90, height = 30)

lblChart1 = tk.Label(text = "График синуса matplotlib")
lblChart1.place(x = 170, y = 122)

#Добавление кнопки и метки для графика 2
btnChart2 = tk.Button(window, text = "График 2", font = ('Hevletica', 10, 'bold'), command = chart2.plot_chart)
btnChart2.place(x = 40, y = 165, width = 90, height = 30)

lblChart2 = tk.Label(text = "Нормальное распределение")
lblChart2.place(x = 170, y = 172)

#Добавление кнопки и метки для графика 3
btnChart3 = tk.Button(window, text = "График 3", font = ('Hevletica', 10, 'bold'), command = chart3                                   .plot_chart)
btnChart3.place(x = 40, y = 215, width = 90, height = 30)

lblChart3 = tk.Label(text = "Столбчатая диаграмма")
lblChart3.place(x = 172, y = 222)

#Добавление кнопки и метки для графика 4
btnChart2 = tk.Button(window, text = "График 4", font = ('Hevletica', 10, 'bold'), command = chart2.plot_chart2 )
btnChart2.place(x = 40, y = 265, width = 90, height = 30)

lblChart2 = tk.Label(text = "Нормальное распределение - 3 графика ")
lblChart2.place(x = 170, y = 272)

#Добавление кнопки и метки для графика 5
btnChart2 = tk.Button(window, text = "График 5", font = ('Hevletica', 10, 'bold'), command = chart4.plot_chart)
btnChart2.place(x = 40, y = 315, width = 90, height = 30)

lblChart2 = tk.Label(text = "Гистограмма Seaborn ")
lblChart2.place(x = 170, y = 322)

#Добавление кнопки и метки для графика 6
btnChart2 = tk.Button(window, text = "График 6", font = ('Hevletica', 10, 'bold'), command = chart2.plot_chart)
btnChart2.place(x = 40, y = 365, width = 90, height = 30)

lblChart2 = tk.Label(text = "Описание графика ")
lblChart2.place(x = 170, y = 372)

#Добавление кнопки и метки для графика 7
btnChart2 = tk.Button(window, text = "График 7", font = ('Hevletica', 10, 'bold'), command = chart2.plot_chart)
btnChart2.place(x = 40, y = 415, width = 90, height = 30)

lblChart2 = tk.Label(text = "Описание графика ")
lblChart2.place(x = 170, y = 422)

#Добавление кнопки и метки для графика 8
btnChart2 = tk.Button(window, text = "График 8", font = ('Hevletica', 10, 'bold'), command = chart2.plot_chart)
btnChart2.place(x = 40, y = 465, width = 90, height = 30)

lblChart2 = tk.Label(text = "Описание графика ")
lblChart2.place(x = 170, y = 472)

#Добавление кнопки закрытия программы
button_close = tk.Button(window, text = "Закрыть", font = ('Hevletica', 10, 'bold'), command = do_close)
button_close.place(x = 330, y = 500, width = 90, height = 30)

window.mainloop()

