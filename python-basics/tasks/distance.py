def edit_distance(string1, string2):

    if len(string1) > len(string2):
        difference = len(string1) - len(string2)
        print(string1[:difference])


    elif len(string2) > len(string1):
        difference = len(string2) - len(string1)
        string2[:difference]

    else:
        difference = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            difference += 1

    return difference

"""string1 = 'medium'
print(string1)
difference = 3
string1[:difference]
print(string1[:3])"""

arr = ['medium', 'median']
print(edit_distance(arr[0], arr[1])) #2 

