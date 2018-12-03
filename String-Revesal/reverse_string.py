def reverse_string(string):
    """Reverses string and returns it.

    Parameters
    ----------
    string

    Returns
    -------

    """
    # define base case
    to_list = list(string)
    if len(to_list) < 2:
        return to_list
    # set start and stop indexes.
    start = 0
    stop = len(to_list) - 1
    while start < stop:
        # swap values
        end_value = to_list[stop]
        to_list[stop] = to_list[start]
        to_list[start] = end_value
        # move indexes
        start += 1
        stop -= 1
    return ''.join(to_list)


def reverse_string_recur(string):
    if string == '':
        return string
    else:
        return reverse_string(string[1:]) + string[0]


string_list = ['tom', 'baba', 'store', 'worbler']

for string in string_list:
    print(reverse_string(string))
    print(reverse_string_recur(string))
