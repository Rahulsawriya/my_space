#remove duplicacy from list
abc = [{'k':1},{'m':2},{'k':2}, {'k':1}]
seen = set()
abc_new = []
for d in abc:
	t = tuple(d.items())
	if t not in seen:
		seen.add(t)
		abc_new.append(d)
print(abc_new)

"""ab = [1, 2, 3, 4, 5]
print({str(i):"ab" for i in ab})
xy = dict.fromkeys(ab, "num")
print(xy)"""



