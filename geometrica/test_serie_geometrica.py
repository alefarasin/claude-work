import pytest
from serie_geometrica import serie_geometrica


def test_single_term():
    assert serie_geometrica(3, 2, 1) == 3
    assert serie_geometrica(5, 0.5, 1) == 5


def test_ratio_two():
    # 1 + 2 + 4 + 8 = 15
    assert serie_geometrica(1, 2, 4) == 15
    # 2 + 4 + 8 + 16 + 32 = 62
    assert serie_geometrica(2, 2, 5) == 62


def test_ratio_half():
    # 8 + 4 + 2 + 1 = 15
    assert serie_geometrica(8, 0.5, 4) == 15.0


def test_ratio_one():
    # r=1: a + a + a = n*a
    assert serie_geometrica(3, 1, 5) == 15
    assert serie_geometrica(7, 1, 3) == 21


def test_ratio_zero():
    # r=0: only the first term is non-zero
    assert serie_geometrica(5, 0, 1) == 5
    assert serie_geometrica(5, 0, 4) == 5


def test_negative_ratio():
    # 1 - 2 + 4 - 8 = -5
    assert serie_geometrica(1, -2, 4) == -5


def test_float_first_term():
    result = serie_geometrica(0.5, 2, 3)
    assert abs(result - 3.5) < 1e-9


def test_invalid_n_zero():
    with pytest.raises(ValueError):
        serie_geometrica(1, 2, 0)


def test_invalid_n_negative():
    with pytest.raises(ValueError):
        serie_geometrica(1, 2, -3)
