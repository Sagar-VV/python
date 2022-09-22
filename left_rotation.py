arr = list(input().rstrip().split(","))
rotation = 4
def left_rotate():
    for i in range (rotation):
        temp = arr[0]
        arr.remove(arr[0])
        arr.append(temp)

    return arr 

a = left_rotate()
print (a)