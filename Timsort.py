import random
import time

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1
        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return list(merge(left, right))

def timsort(arr, min_run=16):
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = min((start + size - 1), (n - 1))
            end = min((start + size * 2 - 1), (n - 1))
            merged_array = merge(left=arr[start:midpoint + 1], right=arr[midpoint + 1:end + 1])
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

def measure_runtime(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Generate and shuffle test data

# Test case: Short list
print(" ")
print(" ")
print("Short list (10 elements):")
print(" ")
test_case_5 = [random.randint(1, 100) for _ in range(10)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_5))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_5))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_5))
# Test case: Empty list
print(" ")
print(" ")
print("Empty list:")
print(" ")
test_case_6 = []
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_6))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_6))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_6))

# Test case: Unsorted list
print(" ")
print(" ")
print("Unsorted list:")
print(" ")
test_case_7 = [random.randint(1, 100) for _ in range(100)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_7))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_7))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_7))

# Test case: Sorted list
print(" ")
print(" ")
print("Sorted list:")
print(" ")
test_case_8 = [i for i in range(1, 101)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_8))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_8))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_8))

# Test case: 10,000 elements
print(" ")
print(" ")
print("Long list (10,000 elements):")
print(" ")
test_case_9 = [random.randint(1, 100) for _ in range(10000)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_9))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_9))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_9))

# Test case: 5,000 elements
print(" ")
print(" ")
print("5,000 elements:")
print(" ")
test_case_10 = [random.randint(1, 100) for _ in range(5000)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_10))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_10))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_10))

# Test case: 1,000 elements
print(" ")
print(" ")
print("1,000 elements:")
print(" ")
test_case_11 = [random.randint(1, 100) for _ in range(1000)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_11))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_11))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_11))

# Test case: Float Data
print(" ")
print(" ")
print("Float data (10 elements):")
print(" ")
test_case_12 = [random.uniform(1.0, 100.0) for _ in range(10)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_12))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_12))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_12))

# Test case: Short list with negative values
print(" ")
print(" ")
print("Short list (10 elements with negative values):")
print(" ")
test_case_13 = [random.randint(-100, 100) for _ in range(10)]
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_13))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_13))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_13))

# Test case: Letters
print(" ")
print(" ")
print("Letters:")
print(" ")
test_case_14 = ['f', 'd', 'a', 'c', 'e', 'b']
print("Timsort runtime:", measure_runtime(lambda arr: timsort(arr, min_run=8), test_case_14))
print("Insertion Sort runtime:", measure_runtime(insertion_sort, test_case_14))
print("Merge Sort runtime:", measure_runtime(merge_sort, test_case_14))