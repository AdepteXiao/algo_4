from heap_sort import heap_sort
from quick_sort import partition
from math import log2


def my_sort(array, begin=0, end=None, depth=0, *, reverse=False):
    if end is None:
        end = len(array) - 1
    if len(array) != 0:
        if depth < log2(len(array)):
            if begin < end:
                mid = partition(array, begin, end, reverse=reverse)
                my_sort(array, begin, mid - 1, depth + 1, reverse=reverse)
                my_sort(array, mid + 1, end, depth + 1, reverse=reverse)
        else:
            array[begin:end + 1] = heap_sort(array[begin:end + 1], reverse=reverse)
    else:
        return array


if __name__ == '__main__':
    b = []
    a = sorted([])
    my_sort(b)
    print(a == b)
