import pytest
from primo import primo


def test_below_two():
    assert primo(0) == []
    assert primo(1) == []


def test_small_values():
    assert primo(2) == [2]
    assert primo(3) == [2, 3]
    assert primo(10) == [2, 3, 5, 7]
    assert primo(20) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_includes_n_when_prime():
    assert primo(13) == [2, 3, 5, 7, 11, 13]


def test_excludes_n_when_not_prime():
    assert primo(15) == [2, 3, 5, 7, 11, 13]


def test_larger_value():
    result = primo(50)
    assert result == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def test_negative_raises():
    with pytest.raises(ValueError):
        primo(-1)
