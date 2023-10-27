# <div align="center">Project 1 - Hybrid and Adaptive Sorting Algorithms</div>
# ***Project Goals***
The goal of this project is to create a hybrid sorting algorithm that combine two sorting techniques and compare the eficiency of all three. The hybrid sorting algorithm that I chose to use was the Timsort sorting algorithm, which combines insertion sort and merge sort sorting techniques. I will compare the time complexities and run time of all three sorting algorithms. Using several test cases to test the efficiency of each one.

# ***Algorithm Description***
The hybrid sorting algorithm I decided to use was Timsort, which combines insertion sort and merge sort sorting techniques.

**Insertion Sort:**
Insertion Sort is a simple comparison-based sorting algorithm that iterates through an array from left to right, considering one element at a time and inserting the element into its correct position within the already sorted part of the array.

When the size of the runs is smaller than a certain threshold, Timsort uses insertion sort to sort these small runs. Insertion sort is an efficient algorithm for small datasets or nearly sorted sequences. Using insertion sort for small runs takes advantage of its simplicity and speed for such cases.

**Merge sort:**
Merge Sort is a divide-and-conquer sorting algorithm that works by dividing an unsorted list into smaller sublists until each sublist consists of one element left, merging these sublists back together in a sorted manner by comparing and combining the elements.

Timsort initially divides the input data into smaller groups, or "runs," which are individually sorted using insertion sort (for small runs). After this step, the sorted runs are combined using a modified merge sort algorithm. Merge sort is used for this merging process, as it is an efficient algorithm for combining two or more sorted sequences into a single sorted sequence.


**Timsort:**
By combining these two sorting algorithms and taking advantage of their strengths, Timsort is able to efficiently sort a wide range of data types, including partially ordered or partially structured data, while maintaining stability in the sorting process. Timsort's adaptive nature, which adjusts its strategy based on the input data, helps it perform well in various scenarios.

**Code Explanation:**

n = len(arr): Determine the length of the input array arr, which is the total number of elements to be sorted.

Initial Insertion Sort Runs:

The input array is divided into smaller runs of size min_run.
For each run, the insertion_sort function is called to sort that run in-place.
The range for each run is determined by i and min_run, ensuring it doesn't exceed the array's bounds.
size = min_run: Set the initial size of runs to min_run.

Merge and Expand Runs:

The algorithm now enters the merge and expand phase, where it combines adjacent runs to create larger sorted runs.
A loop iterates over the array, and for each pair of runs, it merges them using the merge function.
The start, midpoint, and end variables define the indices for the current pair of runs.
The merged run is stored in merged_array.
Finally, the original runs in the array are replaced by the merged run.
size *= 2: After merging a pair of runs, the size of the runs is doubled for the next iteration of the loop. This process continues until the entire array is sorted.

# ***Benchmarking Results***
For my test cases, I tested the three algorithms (Timsort, Insertion sort, and Merge sort) using different scenarios to 

| List Size | TimSort Time| MergeSort Time| QuickSort Time|
| -------- | -------  | --------| --------|
| 10  | 0.0 (Sec)      | 0.0 (Sec)  | 0.0 (Sec)|
| 100 |  0.0 (Sec)     |0.0 (Sec)  | 0.0 (Sec)|
|1000 |  0.002 (Sec)   |0.0025 (Sec)|0.0019 (Sec)|
|10,000| 0.0229 (Sec)  |0.029 (Sec)| 0.0189 (Sec) |
|100,000|  0.3717 (Sec)|0.389 (Sec)| 0.572 (Sec)|
|1,000,000| 4.13 (Sec) |4.29 (Sec) |Failed: Max Recusion Depth|

# ***Numerical Result and Theoretical Analysis***
+ start here
