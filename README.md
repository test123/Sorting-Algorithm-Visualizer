# Sorting algorithm visualizer

Visualizing sorting algorithms, using the matplotlib library.

Algorithms covered so far: 

| Name | Function Name |
| - |:-: |
| Quick Sort | quick_sort |
| Bubble Sort | bubble_sort |
| Selection Sort | selection_sort |
| Insertion Sort | insertion_sort |
| Heap Sort | heap_sort |
| Merge Sort | merge_sort |

# Usage:

Install

```pip install -r requirements.txt``` 

Run

```python main.py function_name```

Pass function name as a command line argument from list of functions above
(in all lower case and spaces replaced by underscore).

**For example:** 

```python main.py quick_sort```

# How to contribute

**If you want to add a new sorting algorithm:**

1. Code the algorithm in ```sorting.py```.
2. Name the function appropriately, like ```quick_sort```, ```bubble_sort```.
3. While coding the function, **do not use python lists**. Instead, use an ```Array``` object. The ```Array``` class is defined in ```sorting.py```. (See already implemented algorithms, for your reference)
4. The ```Array``` object has ```swap```, ```set```, ```get_len```, ```get``` methods implemented. Feel free to implement any more, additional methods, that you may see fit.
5. Make sure you add the sorting algorithm to the Readme file!
6. Make sure your newly implemented algorithm works, by running `test.py` after appending it to the list of algorithms in `test.py`.
