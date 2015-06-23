from datetime import datetime
import math
import vsop.vsop87

class Planet:
    _X = None
    _Y = None
    _Z = None
    
    def __init__(self, *args, **kwargs):
        self._ensure_data()

    @staticmethod
    def _coord_at(data, t):
        res = 0.0
        for n, ABC in data.items():
            x = 0.0
            for A, B, C in ABC:
                x += A * math.cos(B + t * C)
            x *= t ** n
            res += x
        return res

    def position_at(self, day):
        '''Calculates the location of the planet at a particular day and time.

        Returns rectangular coordinates X, Y, Z.
        '''
        t = ((day - datetime(2000, 1, 1, 12)).total_seconds()) / (24 * 60 * 60 * 365250)
        X = self._coord_at(self._X, t)
        Y = self._coord_at(self._Y, t)
        Z = self._coord_at(self._Z, t)
        return X, Y, Z

    @classmethod
    def _ensure_data(cls):
        if cls._X is not None:
            return
        X, Y, Z = {}, {}, {}
        for c, n, A, B, C in vsop.vsop87.read_data(cls._vsop_code, cls._vsop_index):
            data = [X, Y, Z][c]
            data.setdefault(n, []).append((A, B, C))
        cls._X = X
        cls._Y = Y
        cls._Z = Z

class Mercury(Planet):
    _vsop_code = 'mer'
    _vsop_index = 1

class Venus(Planet):
    _vsop_code = 'ven'
    _vsop_index = 2

class Earth(Planet):
    _vsop_code = 'ear'
    _vsop_index = 3

class Mars(Planet):
    _vsop_code = 'mar'
    _vsop_index = 4

class Jupiter(Planet):
    _vsop_code = 'jup'
    _vsop_index = 5

class Saturn(Planet):
    _vsop_code = 'sat'
    _vsop_index = 6

class Uranus(Planet):
    _vsop_code = 'ura'
    _vsop_index = 7

class Neptune(Planet):
    _vsop_code = 'nep'
    _vsop_index = 8
