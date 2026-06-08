def serie_geometrica(a: float, r: float, n: int) -> float:
    """Calcola la somma della serie geometrica: a + a*r + a*r^2 + ... + a*r^(n-1)"""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if r == 1:
        return a * n
    return a * (1 - r**n) / (1 - r)
