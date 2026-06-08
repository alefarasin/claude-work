import pytest
from armonica import armonica


def test_n1():
    assert armonica(1) == 1.0


def test_n2():
    assert armonica(2) == pytest.approx(1.5)


def test_n4():
    # 1 + 1/2 + 1/3 + 1/4 = 25/12
    assert armonica(4) == pytest.approx(25 / 12)


def test_n10():
    expected = sum(1 / k for k in range(1, 11))
    assert armonica(10) == pytest.approx(expected)


def test_increasing():
    assert armonica(2) > armonica(1)
    assert armonica(10) > armonica(5)


def test_zero_raises():
    with pytest.raises(ValueError):
        armonica(0)


def test_negative_raises():
    with pytest.raises(ValueError):
        armonica(-5)


def test_float_raises():
    with pytest.raises(TypeError):
        armonica(3.0)


def test_bool_raises():
    with pytest.raises(TypeError):
        armonica(True)
