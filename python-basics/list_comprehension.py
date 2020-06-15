"""list comprehension: it is an elegant way to define and create lists based on existing lists.
We can create lists using a single line of code (loop & if-else in single line of code).
In list comprehension, we can use map, reduce & filter functions"""

#Find common numbers from two lists using list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)
