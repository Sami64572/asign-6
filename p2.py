#Diamond Problem:
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()
obj.show() 






#Attribute Name Clashes:
class Parent1:
    common_attribute = "Attribute from Parent1"

class Parent2:
    common_attribute = "Attribute from Parent2"

class Child(Parent1, Parent2):
    pass

obj = Child()
print(obj.common_attribute) 






#Complex Inheritance Hierarchies:
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

class C(A):
    def show(self):
        print("Class C")

class D(B, C):
    def show(self):
        super().show() 
        print("Class D")

obj = D()
obj.show()
