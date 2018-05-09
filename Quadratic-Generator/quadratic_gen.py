def quadratic_gen(a, b, c, start=0, step=1):
    """Yields result of a quadratic equation y = ax^2 + bx + c.

    Starting point for calculation is start and the interval is step.

    Parameters
    ----------
    a : float
        Parameter of the equation.
    b : float
            Parameter of the equation.
    c : float
            Parameter of the equation.
    start : float, default 0, optional
        Starting point for the calculation
    step: float, default 1, optional
        Interval for the calculation
    Yields
    -------
    y : float
        Result of the calculation.
    """
    while True:
        y = a * start ** 2 + b * start + c
        yield [start, y]
        start += step