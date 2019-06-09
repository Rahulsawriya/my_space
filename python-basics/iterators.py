#Iterator: An iterator is an object that represents a stream of data, unlike a sequence.
#Its used built in function iter.
#An iterator can only provide the next item.
#its give list iter object through next method, you can move to next element.
a = [1, 2, 3, 4, 5]
print(dir(a))
itr = iter(a)
print(next(itr))