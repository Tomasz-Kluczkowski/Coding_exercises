import time
import random


def nth_smallest(arr, n):
    if n > len(arr):
        return None
    to_set = set(arr)
    sorted_list = sorted(to_set)
    n = n - 1
    if n > len(sorted_list) - 1:
        return None
    return sorted_list[n]


def nth_smallest_order_n(arr, n):
    if n > len(arr):
        return None
    container = []
    smallest = arr[0]

    for i in range(n):

        for item in arr:
            if item < smallest:
                smallest = item
        container.append(smallest)
    if n > len(container):
        return None
    return container[n - 1]


def select(data, n):
    """Find the nth rank ordered element (the least value has rank 0)."""
    data = list(data)
    if not 0 <= n < len(data):
        raise ValueError('not enough elements for the given rank')
    while True:
        pivot = random.choice(data)
        pcount = 0
        under, over = [], []
        uappend, oappend = under.append, over.append
        for elem in data:
            if elem < pivot:
                uappend(elem)
            elif elem > pivot:
                oappend(elem)
            else:
                pcount += 1
        if n < len(under):
            data = under
        elif n < len(under) + pcount:
            return pivot
        else:
            data = over
            n -= len(under) + pcount


def timer(func, arr, n):
    start_time = time.time()
    func(arr, n)
    stop_time = time.time()
    delta = stop_time - start_time
    return delta


if __name__ == '__main__':
    start_time = time.time()
    length = 100000
    setup_arr = [random.randint(1, 100000) for _ in range(length)]
    end_time = time.time()
    delta = end_time - start_time
    print("time to build a list")
    print(delta)

    functions_list = [nth_smallest, nth_smallest_order_n, select]
    for func in functions_list:
        print("time for", func.__name__, timer(func, setup_arr, 123))
