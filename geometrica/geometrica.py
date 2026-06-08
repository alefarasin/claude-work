def serie_geometrica(a: float, r: float, n: int) -> list[float]:
    """Calcola i primi n termini della serie geometrica: a, a*r, a*r^2, ..., a*r^(n-1)."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return [a * (r ** i) for i in range(n)]


def somma_serie_geometrica(a: float, r: float, n: int) -> float:
    """Calcola la somma dei primi n termini della serie geometrica."""
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0.0
    if r == 1:
        return float(a * n)
    return float(a * (1 - r ** n) / (1 - r))
