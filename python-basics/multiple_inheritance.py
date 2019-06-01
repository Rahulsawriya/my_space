#python supports multiple inheritance
class Parent1:
    def func1(self):
        print('parent_1')

class Parent2:
    def func2(self):
        print('parent_2')

class Child(Parent1, Parent2):
    def func3(self):
        print('child')
obj = Child()
obj.func1()
obj.func2()
obj.func3()
