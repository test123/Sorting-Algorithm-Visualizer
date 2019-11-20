import matplotlib.pyplot as plt


def plot(arr):
    plt.clf()
    plt.bar(range(len(arr)), arr, align='edge', width=1, data=arr)
    plt.pause(0.001)


def show():
    plt.show()


fig, graph = plt.subplots()
graph.yaxis.set_visible(False)
graph.xaxis.set_visible(False)
