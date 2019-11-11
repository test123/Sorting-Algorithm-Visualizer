import sorting as s
import numpy as np


def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


def test(sorting_function):
    arr = s.Array(np.random.randint(low=-2000, high=2000, size=1000))
    sorting_function(arr)
    return 'Passed' if is_sorted(arr.values) else 'FAIL'


functions = [s.bubble_sort, s.heap_sort, s.selection_sort,
             s.insertion_sort, s.quick_sort]
for function in functions:
    print('Testing:   ', function.__name__.ljust(16), test(function))
