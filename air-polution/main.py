import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
import lib.gui.view.window as Window
import lib.math as Math

win = Window.gen()
interval = Math.interval()
win.setTitle('PM2.5趨勢監測器')
win.addWidget(signal='combobox', name='comboYear', x=10, y=10)
win.addWidget(signal='label', name='labelYear', text='年', x=70, y=10)
win.addWidget(signal='combobox', name='comboMonth', x=100, y=10)
win.addWidget(signal='label', name='labelMonth', text='月', x=160, y=10)
win.addWidget(signal='combobox', name='comboDay', x=190, y=10)
win.addWidget(signal='label', name='labelDay', text='日', x=250, y=10)
win.addWidget(signal='combobox', name='comboStation', x=280, y=10)
win.addWidget(signal='button', name='buttonSelect', text='查詢', x=380, y=8)
win.addCanvas(name='graph', data=[2, 3, 4, 6, 3])

win.widget['comboYear'].configure(width=5)
win.widget['comboMonth'].configure(width=5)
win.widget['comboDay'].configure(width=5)
win.widget['comboStation'].configure(width=8)

win.widget['comboYear']['value'] = interval.get(low=88, high=105)
win.widget['comboMonth']['value'] = interval.get(low=1, high=12)
win.widget['comboDay']['value'] = interval.get(low=1, high=31)

#win.addEventListener('button1', '<Button-1>', win.showCalendar)
win.run()
