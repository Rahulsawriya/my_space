#Python generators are a simple way of creating iterators. 
#Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
def remote_control_next():
	yield "espn"
	yield "set max"
	yield "aaj tak"

itr = remote_control_next()
print(next(itr))
print("="*50)

#fibonacci series using generators
def fib():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b

for f in fib():
	if f > 50:
		break
	print(f)