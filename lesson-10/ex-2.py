class Road:
    _length = None
    _width = None
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    def formula(self):
        m = self._length * self._width * 25 * 5
        return m

c = Road(10, 10)
print(c.formula())