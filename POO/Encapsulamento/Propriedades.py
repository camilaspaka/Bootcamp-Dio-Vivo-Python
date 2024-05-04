class Foo:
    def _init_(self, x=None):
        self._x = x

    def x(self):
        return self._x or 0
    
    def x(self, value):
        _x = self._x or 0
        _value = value or 0
        self._x = _x + _value

    def x(self):
        self._x = -1

foo = Foo()
print(foo.x)
foo.x = 10
del foo.x
print(foo.x)
