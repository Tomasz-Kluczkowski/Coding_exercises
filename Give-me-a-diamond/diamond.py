def diamond(n):
    """Display a diamond made of *.

    Args:
        n: (int) Amount of *s in the middle row.

    Returns:
        Diamond shaped text. None if input n is invalid.
    """

    if n <= 0 or n % 2 == 0:

        return None

    offset = int((n - 1)/2)

    # for i in range(offset + 1):
    #     shape = shape + " "*(offset - i) + "*"*(1 + i*2) + "\n"

    shape = [(" "*(offset - i) + "*"*(1 + i*2) + "\n") for i in range(offset + 1)]
    shape = shape + shape[-2::-1]

    return ''.join(shape)


print(diamond(29))
print('    *\n   ***\n  *****\n *******\n*********\n *******\n  *****\n'
      '   ***\n    *\n')

    # __*__
    # _***
    # *****
    # _***_
    # __*__

