s = "hello"
# #print s[::-1]
#===========first solution ==============
result = ""
for i in xrange(len(s)-1,-1,-1):  #xrange(start_point, Endpoint, difference)
	result += s[i] 
print result
#================second solution =============
for i in reversed(s):
	result += i
print result



