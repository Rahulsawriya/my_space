#Lists are mutable and tuples are immutable. Just consider this example.

a = ["1", "2", "ra", "sa"]    #list
b = ("1", "2", "ra", "sa")    #tuple

#Now change index values of list and tuple.

a[2] = 1000
print(a)     #output : ['1', '2', 1000, 'sa']
b[2] = 1000
print(b)     #output : TypeError: 'tuple' object does not support item assignment.

#Hence proved the following code is invalid with tuple, because we attempted to update a tuple, which is not allowed.

