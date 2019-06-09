#map function: this function is applied to all the elements of a sequence.
#it returns an iterator to the sequence.
#map(function, sequence)
def sqr(x):
	return x * x
ls = [1, 2, 3, 4, 5]
print(list(map(sqr, ls))) #output: [1, 4, 9, 16, 25]

#filter function: apply the function basis on creteria

#find the odd number
ll = [1, 2, 3, 4, 5, 6, 7, 8]
ff = filter(lambda x: x%2 != 0, ll)
print(list(ff)) #output: [1, 3, 5, 7]

#reduce function: it gives single output at a time, this function is defined in "functools" module.
from functools import reduce
rp = reduce(lambda x, y: x*y, [1, 2, 3, 4])
print(rp)