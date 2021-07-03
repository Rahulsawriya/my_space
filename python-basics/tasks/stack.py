class Stack():
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)
		print(self.stack)

	def pop(self):
		return self.stack[:-1]

obj = Stack()
obj.push('a')
obj.push('b')
obj.push('c')
print(obj.pop())
#print(obj.push('b'))
#Stack.pop()
#print(obj.pop())