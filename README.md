# Sorting algorithm visualizer

Visualizing sorting algorithms, using the matplotlib library.

Algorithms covered so far:<br />
Quick Sort<br />
Bubble Sort<br />
Selection Sort<br />
Insertion Sort<br />
Heap Sort<br />
Merge Sort

# Usage:

Run

```python main.py function_name```

Choose function name from list of functions above (in all lower case and spaces replaced by underscore).

For example: 

```python main.py quick_sort```

# How to contribute

Add new sorting algorithms to `sorting.py`  
In your algorithms, pass an `Array` (defined in `sorting.py`) object, instead of a list.  
  
The call to your sorting algorithm should be `sorting_algorithm(Array([1, 2, 3]))`, not `sorting_algorithm([1, 2, 3])`.  
  
Whenever you are swapping values, call `Array.swap`, and whenever you are setting a value, call `Array.set`.
The length of the array can be found out using `Array.length`.

Make sure you test your newly implemented algorithm by running `test.py` after appending it to the list of algorithms in `test.py`.

