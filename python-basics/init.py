#__init__ is a reseved method in python classes. It is known as a constructor in object oriented concepts. 
#This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
class User:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def emp(self):
		print(self.age)
obj = User("Rahul", 24)
obj.emp()
