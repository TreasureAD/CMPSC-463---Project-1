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
For my test cases, I tested the three algorithms (Timsort, Insertion sort, and Merge sort) using different scenarios to test and compare the effeciency of each algorithm. I did 5 test cases which were a sorted list, unsorted list, long list (10,000 elements), short list (10 elements), and an empty list.

Below are the benchmarking results for each algorithm and each test case.

| Test Case | TimSort Run time| Merge Sort Run time| Insertion Sort Run time|
| -------- | -------  | --------| --------|
| Sorted List  | 0.0002446174621582031 | 0.0006351470947265625| 5.125999450683594e-05|
| Unsorted List | 0.0003635883331298828 |2.7179718017578125e-05  | 0.0005280971527099609|
|10 elements |3.314018249511719e-05|4.00543212890625e-05|4.76837158203125e-06|
|1,000 elements | 0.0037691593170166016   | 0.0074808597564697266  |  0.00020170211791992188   |
|5,000 elements | 0.05072808265686035   |  0.043798208236694336  |  0.0012271404266357422  |
|10,000 elements| 0.11567068099975586  |0.16532373428344727| 0.003881216049194336 |
|Float data (10 elements) | 4.601478576660156e-05   | 6.866455078125e-05   |  4.76837158203125e-06  |
|Include negative values (10 elements) |  3.62396240234375e-05  | 5.9604644775390625e-06   |  6.031990051269531e-05  |
|Letter values |  1.2159347534179688e-05  |  1.8358230590820312e-05  |   3.0994415283203125e-06 |
|Empty List|  1.4543533325195312e-05|1.9073486328125e-06| 6.198883056640625e-06|

# ***Numerical Result and Theoretical Analysis***
+ start here
