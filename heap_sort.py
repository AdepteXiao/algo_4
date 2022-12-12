def percolate_down(heap, idx, max_idx=None, *, reverse=False):
    if max_idx is None:
        max_idx = len(heap) - 1
    while idx < max_idx:
        largest_idx = idx
        if 2 * idx + 1 <= max_idx and (reverse != (heap[2 * idx + 1] > heap[largest_idx])):
            largest_idx = 2 * idx + 1
        if 2 * idx + 2 <= max_idx and (reverse != (heap[2 * idx + 2] > heap[largest_idx])):
            largest_idx = 2 * idx + 2

        if largest_idx != idx:
            heap[idx], heap[largest_idx] = heap[largest_idx], heap[idx]
            idx = largest_idx
        else:
            break


def heapify(heap, max_idx=None, *, reverse=False):
    if max_idx is None:
        max_idx = len(heap) - 1
    for idx in range(max_idx // 2, -1, -1):
        percolate_down(heap, idx, reverse=reverse)


def heap_sort(heap, reverse=False):
    heapify(heap, reverse=reverse)
    for idx in range(len(heap) - 1, 0, -1):
        heap[0], heap[idx] = heap[idx], heap[0]
        percolate_down(heap, 0, idx - 1, reverse=reverse)
    return heap


if __name__ == '__main__':
    a = [3, 4, 6, 3, 1, 2, 5, 9]
    heap_sort(a, reverse=True)
    print(a)





