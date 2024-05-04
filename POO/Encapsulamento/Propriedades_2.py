class Foo:
    def _init_(self, x=None):
        self._x = x

    @property
    def x(self):
        return self._x or 0

foo = Foo()
print(foo.x)
