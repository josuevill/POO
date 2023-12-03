class A:
    def hablar(self):
        print("Hola desde A")

class F(A):
    def hablar(self):
        print("Hola desde B")

class B(A):
    def hablar(self):
        print("Hola desde B")

class C(A):
    def hablar(self):
        print("Hola desde C")

class D(B,C):
    def hablar(self):
        print("Hola desde D")

d = D()

F.hablar(d)

print(D.mro())