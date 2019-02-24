class Class():
    def add(self, x, y):
        print(x + y)
inst = Class()
def not_exactly_add(self, x, y):
    print(x * y)
Class.add = not_exactly_add
inst.add(3, 3)

#Monkey patching is reopening the existing classes or methods in class at runtime and changing the behavior, which should be used 
#cautiously, or you should use it only when you really need to. As Python is a dynamic programming language, Classes are mutable so 
#you can reopen them and modify or even replace them.
