class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        return ("A.x")
    def y(self):
        return ("A.y")
    def z(self):
        return ("A.z")

class B(A):                     
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        return ("B.y")
    def z(self):
        return ("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        return ("C.y")
    def z(self):
        return ("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        return ("D.z")

aobj = A()
bobj = B()
cobj = C()
dobj = D()

print("aobj.x(): "+str(aobj.x()))
print("aobj.y(): "+str(aobj.y()))
print("aobj.z(): "+str(aobj.z()))
print("\n")
print("bobj.x(): "+str(bobj.x()))
print("bobj.y(): "+str(bobj.y()))
print("bobj.z(): "+str(bobj.z()))
print("\n")
print("cobj.y(): "+str(cobj.y()))
print("cobj.z(): "+str(cobj.z()))
print("\n")
print("dobj.x(): "+str(dobj.x()))
print("dobj.y(): "+str(dobj.y()))
print("dobj.z(): "+str(dobj.z()))

# # a(1)
# def a(x):
#     return x+1
# print(a(1))
# def a(x, y):
#     return x+y
# # print(a(1))
# print(a(1,2))
# def a(y):
#     return y+2
# print(a(1))
