def reverse(arr,n):

    arr[0],arr[-1] = arr[-1],arr[0]
    
    return arr
    
def main():
    n = int(input())
    arr = []
    for i in range(n):
        val = int(input())
        arr.append(val)
    # arr.reverse()
    # print(arr)
    reverse(arr,n)
    
    for i in range(n):
        print(arr[i], end = " ")
        
main()
# def main():
#     n = (int(input("Enter length of an array: ")))
#     arr = (int(input("Enter array: ")))
#     reverse(arr, n)
        
main()
