from math import log2


def my_sort(array: list, reverse: bool = False, key=None, cmp=None) -> list:
    ar_len = len(array)
    last_index = ar_len - 1

    key = key if key is not None else lambda x: x
    cmp = cmp if cmp is not None else lambda x, y: x < y

    def intro_sort(begin=0, end=None, depth=0):
        def heap_sort(heap):

            last_heap_index = len(heap) - 1

            def percolate_down(idx, max_idx=None):
                if max_idx is None:
                    max_idx = last_heap_index
                while idx < max_idx:
                    largest_idx = idx
                    left = 2 * idx + 1
                    right = 2 * idx + 2

                    if left <= max_idx and (reverse == cmp(key(heap[left]),
                                                           key(heap[largest_idx]))):
                        largest_idx = left
                    if right <= max_idx and (reverse == cmp(key(heap[right]),
                                                            key(heap[largest_idx]))):
                        largest_idx = right

                    if largest_idx != idx:
                        heap[idx], heap[largest_idx] = heap[largest_idx], heap[idx]
                        idx = largest_idx
                    else:
                        break

            # heapify
            for index in range(last_heap_index // 2, -1, -1):
                percolate_down(index)

            for index in range(last_heap_index, 0, -1):
                heap[0], heap[index] = heap[index], heap[0]
                percolate_down(0, index - 1)
            return heap

        def partition():
            pivot_idx = begin
            pivot = array[pivot_idx]

            array[end], array[pivot_idx] = array[pivot_idx], array[end]
            first_larger = begin
            for idx in range(begin, end):
                if reverse != cmp(key(array[idx]), key(pivot)):
                    array[idx], array[first_larger] = array[first_larger], array[idx]
                    first_larger += 1

            array[end], array[first_larger] = array[first_larger], array[end]
            return first_larger

        if end is None:
            end = last_index
        if ar_len != 0:
            if depth < log2(ar_len):
                if begin < end:
                    mid = partition()
                    intro_sort(begin, mid - 1, depth + 1)
                    intro_sort(mid + 1, end, depth + 1)
            else:
                array[begin:end + 1] = heap_sort(array[begin:end + 1])
        else:
            return array

    intro_sort()

    return array


if __name__ == '__main__':
    from random import shuffle

    a = list(range(1, 1000))
    shuffle(a)
    print(a)
    my_sort(a)
    print(a == sorted(a))
