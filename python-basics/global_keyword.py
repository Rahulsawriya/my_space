z = 10
def func():
	global z
	z = 50
	print(z)
func()
print(z)

#through global keyword, we can modified inside a function and change for the entire 
