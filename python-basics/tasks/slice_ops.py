def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l) 
f(3,[1,2,3])
f(2)
f(3)

L = [2,3,4]
M1 = L
M2 = L[:]
print(M1 is M2)
print(type(M1))
print(type(M2))



#a,b,c = (1,2,3)

l = ['ab', 'cd']

print(len(list(map(list, l))))