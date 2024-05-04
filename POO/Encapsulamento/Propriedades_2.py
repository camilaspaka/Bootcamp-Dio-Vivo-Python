class Foo:
    def _init_(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value):
        return self._x + value

foo = Foo()
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)