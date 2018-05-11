def max_number(input_num):
    """Create largest possible number out of the input.

    Parameters
    ----------
    input_num : int
        Positive integer.

    Returns
    -------
    max_num : int
        Maximum number that can be made out of digits present in input_num.
    """
    num_to_str = str(input_num)
    num_to_list = list(num_to_str)
    num_to_list.sort(reverse=True)
    max_str = "".join(num_to_list)
    max_num = int(max_str)

    return max_num
