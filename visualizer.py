import matplotlib.pyplot as plt
import sys


def plot(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, align='edge', width=1, data=arr)
    plt.pause(0.001)


def on_close(event):
    if not sys.argv[0] == 'test.py':
        sys.exit(0)


def show():
    plt.show()


fig, graph = plt.subplots()
fig.canvas.mpl_connect('close_event', on_close)
graph.yaxis.set_visible(False)
graph.xaxis.set_visible(False)
