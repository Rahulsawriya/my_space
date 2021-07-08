#ip: aaabbccccdddddeefffff
#op: 3abb4c5dee5f
lst = 'aaabbccccdddddeefffff'
#'abaabbbbccddffgggg'
ls = list(set(lst))
op = {}
for i in lst:
	if i in op:
		op[i]+=1
	else:
		op[i] = 1
	"""xy = lst.count(i)
	if xy > 2:
		#print(xy)
		#print(i)
		op.append(xy)
		op.append(i)
	else:
		op.append(i)"""
#print(op)
print(op)






