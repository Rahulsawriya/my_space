import re
st = 'rahul pvt Pvt plc 123'
#rst = re.sub('pvt', 'don', st, flags=re.I)
#print(rst)
rst = re.match('rahul', st, flags=re.I) #match work with only start of the string
#print(rst)
rst = re.search('pvt', st, flags=re.I) #search checks for a match anywhere in the string
#print(rst)
#phone = "2004-959-559 # This is Phone Number"
rst = re.sub('pvt|plc', "", st, flags=re.I)
#rst = re.sub('\s', "ll", st, flags=re.I)
print(rst)