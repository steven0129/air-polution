import tkinter as tk

class gen:
	def __init__(self, **kwargs):
		self.win = tk.Tk()
		return super().__init__(**kwargs)

	def setTitle(self, title):
		self.win.title(title)

	def add(self, signal, text, x, y):
		_Widget(signal=signal, win=self.win, text=text, x=x, y=y)

	def run(self):
		self.win.mainloop()

class _Widget:
	def __init__(self, **kwargs):
		print(kwargs)
		self.win = kwargs['win']
		method = ['label', 'button']
		if kwargs['signal'] == method[0]:
			self._Label(kwargs['text'], kwargs['x'], kwargs['y'])
		elif kwargs['signal'] == method[1]:
			self._Button(kwargs['text'], kwargs['x'], kwargs['y'])


	def _Label(self, text, x, y):
		label = tk.Label(self.win, text=text)
		label.place(x=x, y=y)

	def _Button(self, text, x, y):
		button = tk.Button(self.win, text=text)
		button.place(x=x, y=y)
