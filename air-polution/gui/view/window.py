import tkinter as tk

class window:
	def __init__(self, **kwargs):
		self.win = tk.Tk()
		return super().__init__(**kwargs)

	def setTitle(self, title):
		self.win.title(title)

	def run(self):
		self.win.mainloop()