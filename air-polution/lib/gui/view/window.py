import tkinter as tk

class gen:
	def __init__(self, **kwargs):
		self.win = tk.Tk()
		self.widget = {}
		return super().__init__(**kwargs)

	def setTitle(self, title):
		self.win.title(title)

	def add(self, signal, name, text, x, y):
		widget = _Widget(signal=signal, win=self.win, text=text, x=x, y=y)
		self.widget[name] = widget.gen()

	def addEventListener(self, key, signal, callback):
		self.widget[key].bind(signal, callback)

	def run(self):
		self.win.mainloop()

class _Widget:
	def __init__(self, **kwargs):
		print(kwargs)
		self.win = kwargs['win']
		self.signal = kwargs['signal']
		self.text = kwargs['text']
		self.x = kwargs['x']
		self.y = kwargs['y']

	def gen(self):
		method = ['label', 'button']
		if self.signal == method[0]:
			return self._Label(self.text, self.x, self.y)
		elif self.signal == method[1]:
			return self._Button(self.text, self.x, self.y)

	def _Label(self, text, x, y):
		label = tk.Label(self.win, text=text)
		label.place(x=x, y=y)
		return label

	def _Button(self, text, x, y):
		button = tk.Button(self.win, text=text)
		button.place(x=x, y=y)
		return button
