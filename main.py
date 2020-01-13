import sys
import sorting as s
import visualizer as vs
import numpy as np
import random


def get_random_array(length):
    n = list(range(length))
    random.shuffle(n)
    return n


array_size = 50

algorithms = [s.bubble_sort, s.heap_sort, s.selection_sort,
              s.insertion_sort, s.quick_sort, s.insertion_sort, s.merge_sort]

if len(sys.argv) < 2:
    print('Usage:', 'python', sys.argv[0], 'function_name', '\n')
    print('Choose from:', '\n')
    for algorithm in algorithms:
        print(algorithm.__name__)
    print('\n')
    sys.exit(0)

algorithms = list(filter(lambda a: a.__name__ == sys.argv[1], algorithms))
if (len(algorithms) == 0):
    print('Method does not exist.')
else:
    algorithm = algorithms[0]
    arr = s.Array(get_random_array(array_size))
    algorithm(arr)
    vs.show()
