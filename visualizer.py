import sys
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Plotter:
	# initialising all the raw data and additional kwarg for animation function
	def __init__(self, arr, interval=1, title="Bubble Sort", *, 
				repeat=0, window_shape=(7,5), xkcd=0):
		self.is_xkcd = xkcd
		self.arr = arr
		self.title = title
		self.window_shape = window_shape
		self.interval = interval
		self.repeat = repeat
		self.x = np.arange(start=0, stop=arr.shape[1])	# getting size of arr

	@staticmethod
	def on_close(event):
		if not sys.argv[0] == 'test.py':
			sys.exit(0)

	def animate(self, at):
		[self.bar_collections[i].set_height(self.arr[at][i]) for i in range(len(self.bar_collections))]
		# self.fig.canvas.draw()  # forces canavas to draw a frame

	def plot_util(self):
		self.fig, self.graph = plt.subplots(figsize=self.window_shape)
		self.fig.canvas.mpl_connect('close_event', self.on_close)
		self.graph.yaxis.set_visible(False)
		self.graph.xaxis.set_visible(False)
  
		self.graph.text(0, 1.15, self.title, transform=self.graph.transAxes,
						size=24, weight=300, ha='left', va='top')

		self.bar_collections = self.graph.bar(self.x, self.arr[0], align='edge', width=0.5)

		# since the animate method in not returning any thing, thus we are using blit=False
		anim = FuncAnimation(self.fig, self.animate, frames=self.arr.shape[0], 
							interval=self.interval, blit=0, repeat=self.repeat,
							repeat_delay=1000)

		plt.box(False)
		time.sleep(1)
		plt.show()
		anim.event_source.stop()
		del anim
		plt.close()

	def plot(self):
		try:
			if self.is_xkcd:
				with plt.xkcd():
					self.plot_util()
			else:
				self.plot_util()
		except:	pass
