import pytest
from geometrica import serie_geometrica, somma_serie_geometrica


class TestSerieGeometrica:
    def test_zero_termini(self):
        assert serie_geometrica(2, 3, 0) == []

    def test_un_termine(self):
        assert serie_geometrica(5, 2, 1) == [5]

    def test_serie_standard(self):
        assert serie_geometrica(2, 3, 4) == [2, 6, 18, 54]

    def test_ragione_uno(self):
        assert serie_geometrica(4, 1, 5) == [4, 4, 4, 4, 4]

    def test_ragione_zero(self):
        assert serie_geometrica(3, 0, 4) == [3, 0, 0, 0]

    def test_primo_termine_zero(self):
        assert serie_geometrica(0, 5, 3) == [0, 0, 0]

    def test_ragione_frazionaria(self):
        result = serie_geometrica(16, 0.5, 5)
        assert result == [16, 8.0, 4.0, 2.0, 1.0]

    def test_ragione_negativa(self):
        assert serie_geometrica(1, -2, 4) == [1, -2, 4, -8]

    def test_n_negativo_raise(self):
        with pytest.raises(ValueError):
            serie_geometrica(1, 2, -1)


class TestSommaSerieGeometrica:
    def test_zero_termini(self):
        assert somma_serie_geometrica(2, 3, 0) == 0.0

    def test_un_termine(self):
        assert somma_serie_geometrica(5, 2, 1) == 5.0

    def test_somma_standard(self):
        # 1 + 2 + 4 + 8 = 15
        assert somma_serie_geometrica(1, 2, 4) == 15.0

    def test_ragione_uno(self):
        # a=3, r=1, n=5 → 3*5 = 15
        assert somma_serie_geometrica(3, 1, 5) == 15.0

    def test_ragione_frazionaria(self):
        # 16 + 8 + 4 + 2 + 1 = 31
        assert somma_serie_geometrica(16, 0.5, 5) == 31.0

    def test_ragione_negativa(self):
        # 1 + (-2) + 4 + (-8) = -5
        assert somma_serie_geometrica(1, -2, 4) == -5.0

    def test_n_negativo_raise(self):
        with pytest.raises(ValueError):
            somma_serie_geometrica(1, 2, -1)
