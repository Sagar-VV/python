nums = [1,3,5,6]
target = 5

def searchInsert(nums,target):
    
    start = 0
    end = len(nums)
    
    while start <= end :
        mid = (start + end ) // 2
        if nums[mid] == target:
            print (mid)
            break
            print ('inside if')
        elif nums[mid] < target: 
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
    return mid

searchInsert(nums = [1,3,4,5,6], target = 6)