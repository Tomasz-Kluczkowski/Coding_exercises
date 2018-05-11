def binary_search(input_list, item):
    """Simple binary search implementation of a sorted array."""
    # Find mid index.
    first = 0
    last = len(input_list) - 1
    while first <= last:
        mid_ix = (first + last) // 2
        if input_list[mid_ix] == item:
            return mid_ix
        elif input_list[mid_ix] < item:
            first = mid_ix + 1
        else:
            last = mid_ix - 1
    return None


def binary_search_recursive(input_list, item, first=0, last=None):
    """Recursive search for item index."""
    if last is None:
        last = len(input_list) - 1
    if first > last:
        return None
    mid_ix = (first + last) // 2
    if input_list[mid_ix] == item:
        return mid_ix
    elif input_list[mid_ix] < item:
        return binary_search_recursive(input_list, item, mid_ix + 1, last)
    else:
        return binary_search_recursive(input_list, item, first, mid_ix - 1)
