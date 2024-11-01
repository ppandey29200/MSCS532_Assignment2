import time
import random
# Quick Sort Implementation
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort Implementation
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Generate Sorted, reverse sorted, and random datasets
def generate_datasets(size):
    sorted_data = list(range(size))  # Sorted dataset
    reverse_sorted_data = list(range(size, 0, -1))  # Reverse sorted dataset
    random_data = [random.randint(1, 10000) for _ in range(size)]  # Random dataset
    return sorted_data, reverse_sorted_data, random_data

# Measure Performance
def measure_performance(sort_function, data):
    start_time = time.time()
    sorted_data = sort_function(data)
    end_time = time.time()
    return end_time - start_time

# Some Datasets
sizes = [1000, 10000, 100000]
for size in sizes:
    sorted_data, reverse_sorted_data, random_data = generate_datasets(size)

    quick_sort_time_sorted = measure_performance(quick_sort, sorted_data.copy())
    merge_sort_time_sorted = measure_performance(merge_sort, sorted_data.copy())

    quick_sort_time_reverse = measure_performance(quick_sort, reverse_sorted_data.copy())
    merge_sort_time_reverse = measure_performance(merge_sort, reverse_sorted_data.copy())

    quick_sort_time_random = measure_performance(quick_sort, random_data.copy())
    merge_sort_time_random = measure_performance(merge_sort, random_data.copy())

    print(f"Size: {size}")
    print(f"  Quick Sort (Sorted): {quick_sort_time_sorted:.5f}, Merge Sort (Sorted): {merge_sort_time_sorted:.5f}")
    print(f"  Quick Sort (Reverse): {quick_sort_time_reverse:.5f}, Merge Sort (Reverse): {merge_sort_time_reverse:.5f}")
    print(f"  Quick Sort (Random): {quick_sort_time_random:.5f}, Merge Sort (Random): {merge_sort_time_random:.5f}")