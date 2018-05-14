def unique_in_order(input_sequence):
    """Returns list of non repeating items from input sequence retaining
    the order.

    Parameters
    ----------
    input_sequence : sequence
        Any sequence like object.
    Returns
    -------
    unique_items : list
        List of items which do not repeat next to each other.
    """
    if len(input_sequence) > 0:
        to_list = list(input_sequence)
        unique_items = [to_list[0]] + [to_list[ix] for ix in range(1, len(to_list)) if to_list[ix] != to_list[ix - 1]]
        return unique_items
    else:
        return []

