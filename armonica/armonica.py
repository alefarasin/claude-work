def armonica(n: int) -> float:
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
    return sum(1 / k for k in range(1, n + 1))
