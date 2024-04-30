class Cachorro:
    def __del_(self):
        print("Destruindo a instancia")
c = Cachorro()
del c