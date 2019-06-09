#DeepCopy points to a different location in memory, but the contents are the same. Shallow copy is a bit-wise copy of an object.
#shallow copy means that any changes made to a copy of object do reflect in the original object
#deepcopy means that any changes made to a copy of object do not reflect in the original object.
import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

old_list[1][1] = 'bb'
print("shallow copy output")
print("Old list:", old_list)
print("New list:", new_list)

#shallow copy output:
#Old list: [[1, 1, 1], [2, 'bb', 2], [3, 3, 3]]
#New list: [[1, 1, 1], [2, 'bb', 2], [3, 3, 3]]

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list[1][0] = 'BB'
print("deep copy output")
print("Old list:", old_list)
print("New list:", new_list)

# deep copy output
# Old list: [[1, 1, 1], ['BB', 2, 2], [3, 3, 3]]
# New list: [[1, 1, 1], [2, 2, 2], [3, 3, 3]]