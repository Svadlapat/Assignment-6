# selection.py
# Deterministic (Median of Medians) & Randomized Quickselect Algorithms

from typing import List
import random


# ------------------------------------------------------------
# Partition Helper
# ------------------------------------------------------------
def partition(arr: List[int], low: int, high: int, pivot_index: int) -> int:
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    store = low

    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1

    arr[store], arr[high] = arr[high], arr[store]
    return store


# ------------------------------------------------------------
# Randomized Quickselect (Expected O(n))
# ------------------------------------------------------------
def randomized_select(arr: List[int], k: int) -> int:
    if k < 0 or k >= len(arr):
        raise IndexError("k out of range")

    a = list(arr)
    return _randomized_select(a, 0, len(a) - 1, k)


def _randomized_select(a, low, high, k):
    while True:
        if low == high:
            return a[low]

        pivot_index = random.randint(low, high)
        pivot_new_index = partition(a, low, high, pivot_index)

        if k == pivot_new_index:
            return a[k]
        elif k < pivot_new_index:
            high = pivot_new_index - 1
        else:
            low = pivot_new_index + 1


# ------------------------------------------------------------
# Deterministic Median of Medians (Worst-case O(n))
# ------------------------------------------------------------
def deterministic_select(arr: List[int], k: int) -> int:
    if k < 0 or k >= len(arr):
        raise IndexError("k out of range")

    a = list(arr)
    return _deterministic_select(a, 0, len(a) - 1, k)


def _insertion_sort(a, low, high):
    for i in range(low + 1, high + 1):
        key = a[i]
        j = i - 1
        while j >= low and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


def _median_of_small(a, low, high):
    _insertion_sort(a, low, high)
    return (low + high) // 2


def _select_pivot_by_medians(a, low, high):
    n = high - low + 1
    if n <= 5:
        return _median_of_small(a, low, high)

    medians = []
    i = low
    while i <= high:
        sub_high = min(i + 4, high)
        m = _median_of_small(a, i, sub_high)
        medians.append(a[m])
        i += 5

    median_val = deterministic_select(medians, len(medians) // 2)

    # find actual index
    for j in range(low, high + 1):
        if a[j] == median_val:
            return j
    return low


def _deterministic_select(a, low, high, k):
    while True:
        if low == high:
            return a[low]

        pivot_index = _select_pivot_by_medians(a, low, high)
        pivot_new_index = partition(a, low, high, pivot_index)

        if k == pivot_new_index:
            return a[k]
        elif k < pivot_new_index:
            high = pivot_new_index - 1
        else:
            low = pivot_new_index + 1


# Easy wrapper (1-based)
def kth_smallest_randomized(arr, k):
    return randomized_select(arr, k - 1)


def kth_smallest_deterministic(arr, k):
    return deterministic_select(arr, k - 1)
