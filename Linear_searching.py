
list = [2,4,6,8,23,25,11,13,15]
key = 13
n = len(list)

def linear_search(list,n,key):

    for i in range (0,n):
        if (list[i] == key):
            return i
    return -1

result = linear_search(list, n, key)  

if (result == -1):
    print('Element is not found ')
else:
    print('Element is found at index : ' , result)

