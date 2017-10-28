def find_missing(ar_prog):
    """Finds missing item in the arithmetic progression."""

    # The sum of terms of arithmetic progression is:
    # S = n*(a1 + an)/2
    # where in our case since 1 item is missing n = len(ar_prog) +1

    sum_complete = (len(ar_prog) + 1)*(ar_prog[0] + ar_prog[-1])/2
    sum_current = sum(ar_prog)

    return sum_complete - sum_current
