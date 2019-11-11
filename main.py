import sorting as s
import visualizer as vs
import numpy as np
import random


def get_random_array():
    n = list(range(100))
    random.shuffle(n)
    return n


arr = s.Array(get_random_array())
s.selection_sort(arr)
vs.show()
