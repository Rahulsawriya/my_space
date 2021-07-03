old_list = [5, 7, 2, 1]
new_list = []
while old_list:
	minimum = old_list[0]
	for item in old_list:
		if item < minimum:
			minimum = item
	new_list.append(minimum)
	old_list.remove(minimum)
print(new_list)
