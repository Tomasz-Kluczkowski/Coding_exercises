def is_madvah_array(array):
    """Check if array matches condition required for a Madvah Array.

    The Madvah Array has the following property:
    a[0] = a[1] + a[2] = a[3] + a[4] + a[5] = a[6] + a[7] + a[8] + a[9] = ...

    Parameters
    ----------
    array : list(int)
        List of integers.

    Returns
    -------
    Bool
        True if array is Madvah type, false otherwise.
    """
    if len(array) < 3:
        return False
    root_value = array[0]
    ix_bot = 1
    ix_top = 2
    items_to_count = 2
    while ix_top < len(array):
        sum = 0
        for ix in range(ix_bot, ix_top + 1):
            sum += array[ix]
        if sum != root_value:
            return False
        # If at the end of the array and all the sums were equal
        # to the root value.
        elif ix_top == len(array) - 1:
            return True

        items_to_count += 1
        ix_bot = ix_top + 1
        ix_top = ix_top + items_to_count
        if ix_bot > len(array) - 1:
            return False
    return False

