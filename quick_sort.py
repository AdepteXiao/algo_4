import random


def find_pivot(begin, end):
    return random.randint(begin, end)
    # return begin


def partition(array, begin, end, *, reverse=False):
    pivot_idx = find_pivot(begin, end)
    pivot = array[pivot_idx]

    array[end], array[pivot_idx] = array[pivot_idx], array[end]
    first_larger = begin
    for idx in range(begin, end):
        if reverse ^ (array[idx] <= pivot):
            array[idx], array[first_larger] = array[first_larger], array[idx]
            first_larger += 1

    array[end], array[first_larger] = array[first_larger], array[end]
    return first_larger


def quick_sort(array, begin=0, end=None, *, reverse=False):
    if end is None:
        end = len(array) - 1

    if begin < end:
        mid = partition(array, begin, end, reverse=reverse)
        quick_sort(array, begin, mid - 1, reverse=reverse)
        quick_sort(array, mid + 1, end, reverse=reverse)
