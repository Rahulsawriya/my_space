class Animal:
    def eat(self):
        print("eating")
class Dog(Animal):
    def bark(self):
        print("braking")
obj=Dog()
obj.eat()
obj.bark()
