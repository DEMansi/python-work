class A:
    def show (self):
        print("Show From A")

class B:
    def show (slef):
        print("Show From B ")
class C(A,B):
    def show (self):
        print("Show From C")


c1=C()
c1.show()
