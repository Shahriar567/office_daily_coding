import heapq


def _heappush_max(heap, item):
    heap.append(item)
    heapq._siftdown_max(heap, 0, len(heap)-1)


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()  # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        heapq._siftup_max(heap, 0)
        return returnitem
    return lastelt


def heapsort2(iterable):
    h = []
    heapq._heapify_max(h)
    for value in iterable:
        _heappush_max(h, value* value)
    return [_heappop_max(h) for i in range(len(h))]


if __name__ == "__main__":

    #print heapsort([1, 3, 5, 7, 9, 2, 4, 6])
    print heapsort2([-9, -2, 1, 3, 5, 7, 4, 6])




