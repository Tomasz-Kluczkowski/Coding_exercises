def is_merge(complete, part1, part2):
    """Checks if part1 & 2 can be merged into complete maintaining order
    of characters."""

    if len(part1) + len(part2) != len(complete):
        return False

    if part1 in complete:
        ix = complete.find(part1)
        remaining = complete[0:ix] + complete[ix + len(part1):]

        if remaining == part2:
            return True

    if part2 in complete:
        ix = complete.find(part2)
        remaining = complete[0:ix] + complete[ix + len(part2):]

        if remaining == part1:
            return True

    p1ix = 0
    p2ix = 0
    ix = 0

    while ix < len(complete):

        if p1ix < len(part1) and part1[p1ix] == complete[ix]:
            p1ix += 1
            ix += 1
            continue
        elif p2ix < len(part2) and part2[p2ix] == complete[ix]:
            p2ix += 1
            ix += 1
            continue
        else:
            return False

    return True

# 'bananas', 'bas', 'anan', True
