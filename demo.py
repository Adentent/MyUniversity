class A:
    def __init__(self):
        self.a = 100
    class B:
        def b(self):
            print(self.a)


if __name__ == "__main__":
    A = A()
    B = A.B()
    B.b()