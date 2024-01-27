# 1)Method Resolution Order (MRO):
#Python uses the C3 linearization algorithm to determine the order in which base classes are considered during method resolution. The MRO is crucial for resolving the diamond problem and determining which methods or attributes are inherited when a class has multiple parents.

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





# 2)Attribute and Method Name Clashes:
#When two or more parent classes define attributes or methods with the same name, there may be conflicts. The attribute/method resolution follows the MRO, and the first occurrence in the MRO takes precedence.

class Parent1:
    common_attribute = "Attribute from Parent1"

class Parent2:
    common_attribute = "Attribute from Parent2"

class Child(Parent1, Parent2):
    pass

obj = Child()
print(obj.common_attribute) 






# 3)Super() Function Usage:

#The super() function is used to call methods from parent classes in a consistent way. However, its behavior can be affected by the MRO, and the order of base classes becomes important.

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

class C(A):
    def show(self):
        super().show()
        print("Class C")

class D(B, C):
    def show(self):
        super().show()
        print("Class D")

obj = D()
obj.show()





#Order of Base Classes:

# 4)The order in which base classes are specified affects the MRO and can lead to different behavior. Changing the order may have unintended consequences

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

class E(C, B):
    pass

obj_d = D()
obj_d.show() 

obj_e = E()
obj_e.show() 