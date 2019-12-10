#remove method: it takes value as a input, search for it & remove the first match.
a = [0, 2, 3, 2]
a.remove(2) # [0, 3, 2]
#a.remove(7) # Error, x not in list
print(a)

#del function: it removes an item at a specific index, can delete elements or slice.
b = [3, 2, 2, 1]
del b[1]
print(b)
#del b[7] # Error, list assignment index out of range

#pop method: by default, it removes and return the last element but you can pop any element by providing an index.
c = [4, 3, 5]
c.pop(1)
print(c) # [4, 5]
#c.pop(7) #Error, pop index out of range

#del vs. pop
#In pop, you can store pop out value but with del function, you can't
a = [1, 2, 3, 4]
b = a.pop(2)
print(b)
#c = del a[3]
#print(c) #invalid syntax

#append vs insert vs extend
#If we want to add an element at the end of a list, we should use append .
#If we want to add an element at specific index in a list, we should use insert .
#If we want to combine the elements of another iterable to our list, then we should use extend.
a = [1, 2, 3]
a.append(0)
print(a) # [1, 2, 3, 0]
a.insert(1, 5)
print(a) # [1, 5, 2, 3, 0]
a.extend([6, 7, 8])
print(a) # [1, 5, 2, 3, 0, 6, 7, 8] 