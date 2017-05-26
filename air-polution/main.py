import tkinter as tk
from tkinter import messagebox
import lib.gui.view.window as Window
import lib.math as Math

win = Window.gen()
interval = Math.interval()
win.setTitle('PM2.5趨勢監測器')
win.addWidget(signal='combobox', name='comboYear', x=10, y=10)
win.addWidget(signal='label', name='labelYear', text='年', x=80, y=10)
win.addWidget(signal='combobox', name='comboMonth', x=100, y=10)
win.addWidget(signal='label', name='labelMonth', text='月', x=170, y=10)
win.addWidget(signal='combobox', name='comboDay', x=190, y=10)
win.addWidget(signal='label', name='labelDay', text='日', x=260, y=10)
win.addWidget(signal='button', name='button1', text='查詢', x=280, y=10)

win.widget['comboYear'].configure(width=5)
win.widget['comboMonth'].configure(width=5)
win.widget['comboDay'].configure(width=5)

win.widget['comboYear']['value'] = interval.get(low=88, high=105)
win.widget['comboMonth']['value'] = interval.get(low=1, high=12)
win.widget['comboDay']['value'] = interval.get(low=1, high=31)

#win.addEventListener('button1', '<Button-1>', win.showCalendar)
win.run()
