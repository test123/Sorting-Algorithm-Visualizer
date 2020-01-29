from time import sleep
import visualizer as vs

test = False


class Array:

    full_array = None

    def plot(self):
        if not test:
            vs.plot(Array.full_array)

    def set_all(self, values):
        for i in range(len(self.values)):
            self.values[i] = values[i]
        for i in range(len(self.values)):
            Array.full_array[self.lower_index + i] = values[i]
            self.plot()

    def __init__(self, values, lower_index=0):
        self.lower_index = lower_index
        self.values = list(values)

        if Array.full_array == None:
            Array.full_array = list(values)
            self.plot()

    def swap(self, index1, index2):
        self.values[index2], self.values[index1] = self.values[index1], self.values[index2]
        Array.full_array[self.lower_index + index2], Array.full_array[self.lower_index +
                                                                      index1] = Array.full_array[self.lower_index + index1], Array.full_array[self.lower_index + index2]
        self.plot()

    def set(self, index, num):
        self.values[index] = num
        Array.full_array[self.lower_index + index] = num
        self.plot()

    def get_len(self):
        return len(self.values)


def bubble_sort(nums):  # n^2
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(nums.get_len() - 1):
            if nums.values[i] > nums.values[i + 1]:
                # Swap the elements
                nums.swap(i, i + 1)
                # Set the flag to True so we'll loop again
                swapped = True


def selection_sort(nums):  # n^2
    # This value of i corresponds to how many values were sorted
    for i in range(nums.get_len()):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, nums.get_len()):
            if nums.values[j] < nums.values[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums.swap(i, lowest_value_index)


def insertion_sort(nums):  # n^2
    # Start on the second element as we assume the first element is sorted
    for i in range(1, nums.get_len()):
        item_to_insert = nums.values[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums.values[j] > item_to_insert:
            nums.set(j + 1, nums.values[j])
            j -= 1
        # Insert the item
        nums.set(j + 1, item_to_insert)

        
        
        
        

def heap_sort(nums):  # n * logn

    def heapify(nums, heap_size, root_index):
        # Assume the index of the largest element is the root index
        largest = root_index
        left_child = (2 * root_index) + 1
        right_child = (2 * root_index) + 2

        # If the left child of the root is a valid index, and the element is greater
        # than the current largest element, then update the largest element
        if left_child < heap_size and nums.values[left_child] > nums.values[largest]:
            largest = left_child

        # Do the same for the right child of the root
        if right_child < heap_size and nums.values[right_child] > nums.values[largest]:
            largest = right_child

        # If the largest element is no longer the root element, swap them
        if largest != root_index:
            nums.swap(root_index, largest)
            # Heapify the new root element to ensure it's the largest
            heapify(nums, heap_size, largest)

    n = nums.get_len()

    # Create a Max Heap from the list
    # The 2nd argument of range means we stop at the element before -1 i.e.
    # the first element of the list.
    # The 3rd argument of range means we iterate backwards, reducing the count
    # of i by 1
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the root of the max heap to the end of
    for i in range(n - 1, 0, -1):
        nums.swap(i, 0)
        heapify(nums, i, 0)


def merge_sort(nums, lower_index=0):  # n * logn
    def merge(left_list, right_list):
        sorted_list = []
        left_list_index = right_list_index = 0

        # We use the list lengths often, so it's handy to make variables
        left_list_length, right_list_length = len(left_list), len(right_list)

        for _ in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                # We check which value from the start of each list is smaller
                # If the item at the beginning of the left list is smaller, add it
                # to the sorted list
                if left_list[left_list_index] <= right_list[right_list_index]:
                    sorted_list.append(left_list[left_list_index])
                    left_list_index += 1
                # If the item at the beginning of the right list is smaller, add it
                # to the sorted list
                else:
                    sorted_list.append(right_list[right_list_index])
                    right_list_index += 1

            # If we've reached the end of the of the left list, add the elements
            # from the right list
            elif left_list_index == left_list_length:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1
            # If we've reached the end of the of the right list, add the elements
            # from the left list
            elif right_list_index == right_list_length:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

        return sorted_list

    # If the list is a single element, return it
    if nums.get_len() <= 1:
        return nums.values

    # Use floor division to get midpoint, indices must be integers
    mid = nums.get_len() // 2

    # Sort and merge each half
    left_list = merge_sort(Array(nums.values[:mid], lower_index))
    right_list = merge_sort(Array(nums.values[mid:], mid), mid)

    nums.set_all(left_list + right_list)

    # Merge the sorted lists into a new one
    sorted_list = merge(left_list, right_list)

    nums.set_all(sorted_list)
    return sorted_list


def quick_sort(nums):  # n^2
    def partition(nums, low, high):
        # We select the middle element to be the pivot. Some implementations select
        # the first element or the last element. Sometimes the median value becomes
        # the pivot, or a random one. There are many more strategies that can be
        # chosen or created.
        pivot = nums.values[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while nums.values[i] < pivot:
                i += 1

            j -= 1
            while nums.values[j] > pivot:
                j -= 1

            if i >= j:
                return j

            # If an element at i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot), then swap them
            nums.swap(j, i)

    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, nums.get_len() - 1)
    
   
# Python program for implementation of Radix Sort  BY Saugata Debnath  
  
# A function to do counting sort of arr[] according to 
# the digit represented by exp. 
def counting_sort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radix_sort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        counting_sort(arr,exp) 
        exp *= 10
  
